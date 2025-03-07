from django.db import models
from project.utils import hash_generate, handle_image_upload




class Summary(models.Model):
    professional_summary = models.TextField(blank=True, null=True, default='')
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Summary'

    def __str__(self):
        return 'Professional Summary'
    


class Organization(models.Model):
    organization_hash = models.CharField(primary_key=True, default="", max_length=3, blank=True, null=False)
    organization_name = models.CharField(max_length=1000, blank=False, null=False, default='')
    organization_logo = models.ImageField(upload_to='assets/organization', blank=False, null=False, default='')
    organization_logo_alt = models.CharField(max_length=1000, blank=True, null=False, default='')

    def save(self, *args, **kwargs):
        if not self.organization_hash:
            self.organization_hash = hash_generate(3)
        if not self.organization_logo_alt:
            self.organization_logo_alt = f"{self.organization_name.capitalize()}'s Brand Logo"
        super(Organization, self).save(*args, **kwargs)

    
    class Meta:
        ordering = ('organization_name', 'organization_hash',)

    def __str__(self):
        return self.organization_name
    


class Experience(models.Model):
    experience_id = models.CharField(primary_key=True, default="", max_length=5, blank=True, null=False)
    company =  models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=False)
    position = models.CharField(max_length=1000, blank=True, null=True, default='')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    is_published = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        if not self.experience_id:
            self.experience_id = hash_generate(5)
        super(Experience, self).save(*args, **kwargs)


    class Meta:
        ordering = ('company', 'start_date', 'end_date', 'is_published', 'experience_id',)

        
    def __str__(self):
        return f"{self.position} at {self.company}"



class Certification(models.Model):
    certification_hash = models.CharField(primary_key=True, default="", max_length=3, blank=True, null=False)
    institution =  models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=False)
    degree = models.CharField(max_length=1000, blank=True, null=True, default='')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    certification_id = models.CharField(max_length=1000, blank=True, null=True, default='')
    certification_url = models.URLField(blank=True, null=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.certification_hash:
            self.certification_hash = hash_generate(3)
        super(Certification, self).save(*args, **kwargs)

    class Meta:
        ordering = ('degree', 'institution', 'start_date', 'end_date', 'is_published', 'certification_hash',)

    def __str__(self):
        return f"{self.degree} at {self.institution}"
    


class Skill(models.Model):
    skill_id = models.CharField(primary_key=True, default="", max_length=5, blank=True, null=False)
    skill_name = models.CharField(max_length=1000, blank=False, null=False, default='')

    def save(self, *args, **kwargs):
        if not self.skill_id:
            self.skill_id = hash_generate(5)
        super(Skill, self).save(*args, **kwargs)

    class Meta:
        ordering = ('skill_name', 'skill_id',)

    def __str__(self):
        return self.skill_name
    