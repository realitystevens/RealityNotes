from django.contrib import admin
from .models import Article, Tag, WebsiteDescription



admin.site.site_header = 'Reality Notes Administration'
admin.site.site_title = 'Reality Notes'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_hash', 'is_featured', 'published_at',)
    list_filter = ('published_at', 'is_featured',)
    search_fields = ('title__startswith', 'urlhash__startswith', 'published_at__startswith',)
admin.site.register(Article, ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_hash',)
    search_fields = ('tag_name__startswith', 'tag_hash__startswith',)
admin.site.register(Tag, TagAdmin)


class WebsiteDescriptionAdmin(admin.ModelAdmin):
    list_display = ('content', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('content__startswith',)
admin.site.register(WebsiteDescription, WebsiteDescriptionAdmin)
