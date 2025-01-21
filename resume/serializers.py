from rest_framework import serializers
from .models import Organization, Summary, Experience, Skill, Certification




class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['professional_summary']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_name', 'organization_logo', 'organization_logo_alt']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'start_date', 'end_date', 'description']


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = ['institution', 'degree', 'start_date', 'end_date', 'certification_id', 'certification_url', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']
