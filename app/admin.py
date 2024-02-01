from django.contrib import admin
from .models import Article



admin.site.site_header = 'Reality Notes Administration'
admin.site.site_title = 'Reality Notes'


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'url_hash', 'is_featured', 'published_at',)

    list_filter = ('published_at', 'is_featured',)

    search_fields = ('title__startswith', 'urlhash__startswith', 'published_at__startswith',)

admin.site.register(Article, ArticleAdmin)
