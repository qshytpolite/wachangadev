from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse('projects:detail', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.updated_at
