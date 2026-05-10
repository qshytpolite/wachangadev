from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'featured', 'order', 'created_at')
    list_editable = ('featured', 'order')
    list_filter = ('project_type', 'featured')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Core', {
            'fields': ('title', 'slug', 'project_type', 'featured', 'order')
        }),
        ('Content', {
            'fields': ('short_description', 'description', 'image')
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )
