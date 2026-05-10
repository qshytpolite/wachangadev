from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from projects import views as project_views
from projects.sitemaps import ProjectSitemap

sitemaps = {'projects': ProjectSitemap}

urlpatterns = [
    path('admin/portal/', admin.site.urls),  # obscured admin URL
    path('', project_views.home, name='home'),
    path('work/', include('projects.urls')),
    path('contact/', project_views.contact, name='contact'),
    path('robots.txt', project_views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Media files in development (no Cloudinary)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = 'projects.views.error_404'
handler500 = 'projects.views.error_500'
