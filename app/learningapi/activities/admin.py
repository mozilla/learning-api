from django.contrib import admin

from .models import Activity


class TeachingKitInline(admin.StackedInline):
    model = Activity.teaching_kits.through
    verbose_name = 'Teaching Kit'


@admin.register(Activity)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        TeachingKitInline,
    ]
