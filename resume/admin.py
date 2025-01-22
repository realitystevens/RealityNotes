from django.contrib import admin
from .models import Organization, Experience, Skill, Certification, Summary



    
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('professional_summary', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('professional_summary__startswith',)
admin.site.register(Summary, SummaryAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organization_hash',)
    search_fields = ('organization_hash__startswith', 'organization_name__startswith', 'organization_logo_alt__startswith',)
admin.site.register(Organization, OrganizationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'is_published', 'experience_id',)
    list_filter = ('start_date', 'end_date', 'is_published',)
    search_fields = ('experience_id__startswith', 'company__startswith', 'position__startswith', 'start_date__startswith', 'end_date__startswith', 'description__startswith', 'is_published__startswith',)
admin.site.register(Experience, ExperienceAdmin)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'is_published', 'certification_hash', )
    list_filter = ('is_published', 'start_date', 'end_date',)
    search_fields = ('certification_id__startswith', 'institution__startswith', 'degree__startswith', 'certification_url__startswith', 'certification_image_alt__startswith', 'is_published__startswith',)
admin.site.register(Certification, CertificationAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_id',)
    search_fields = ('skill_id__startswith', 'skill_name__startswith',)
admin.site.register(Skill, SkillAdmin)