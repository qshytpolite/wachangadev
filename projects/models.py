from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    TYPE_CHOICES = [
        ('web', 'Web Application'),
        ('data', 'Data Engineering'),
        ('scraping', 'Web Scraping'),
        ('analysis', 'Data Analysis'),
        ('api', 'API / Backend'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='web')
    short_description = models.CharField(
        max_length=180,
        help_text='Shown on the project card (max 180 chars)'
    )
    description = models.TextField(
        help_text='Full project description shown on detail page'
    )
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text='Project screenshot or cover image'
    )
    tags = TaggableManager(
        blank=True,
        help_text='Comma-separated tags e.g. Python, Django, Pandas'
    )
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(
        default=False,
        help_text='Show this project on the homepage'
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lower number = appears first'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
