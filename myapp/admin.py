from django.contrib import admin
from django.utils.safestring import mark_safe

from myapp.models import Organization, Event, User

admin.site.register(User)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'postcode')
    search_fields = ('title', 'address', 'postcode')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'preview')
    search_fields = ('title',)

    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;">')
        else:
            return ''
    preview.short_description = 'Превью'
    preview.allow_tags = True
