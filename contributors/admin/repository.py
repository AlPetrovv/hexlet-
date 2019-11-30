from django.contrib import admin

from contributors.models import Contribution, Repository


class ContributionInline(admin.TabularInline):
    """Contributions of repository."""

    model = Contribution
    extra = 0


class RepositoryAdmin(admin.ModelAdmin):
    """Repository representation."""

    fieldsets = (
        (None, {
            'fields': (
                'is_tracked',
                'name',
                'full_name',
                'html_url',
                'organization',
            ),
        }),
    )
    inlines = (ContributionInline,)
    list_display = ('id', 'name', 'organization', 'is_tracked')
    list_filter = ('organization',)
    search_fields = ('name',)


admin.site.register(Repository, RepositoryAdmin)
