from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .models import Project
from .forms import ContactForm


def home(request):
    featured_projects = Project.objects.filter(featured=True).prefetch_related('tags')
    return render(request, 'home.html', {'featured_projects': featured_projects})


def project_list(request):
    tag = request.GET.get('tag')
    project_type = request.GET.get('type')
    projects = Project.objects.all().prefetch_related('tags')
    if tag:
        projects = projects.filter(tags__name__in=[tag])
    if project_type:
        projects = projects.filter(project_type=project_type)
    return render(request, 'projects/list.html', {
        'projects': projects,
        'type_choices': Project.TYPE_CHOICES,
        'active_tag': tag,
        'active_type': project_type,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.exclude(pk=project.pk).filter(
        project_type=project.project_type
    )[:3]
    return render(request, 'projects/detail.html', {
        'project': project,
        'related': related,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject=f'Portfolio contact from {name}',
                    message=f'From: {name} <{email}>\n\n{message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Message sent — I will get back to you shortly.')
            except Exception:
                messages.error(request, 'Something went wrong. Try emailing directly.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Disallow: /admin/portal/\n"
        f"Sitemap: https://stanleywachanga.dev/sitemap.xml\n"
    )
    return HttpResponse(content, content_type='text/plain')


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    return render(request, 'errors/500.html', status=500)
