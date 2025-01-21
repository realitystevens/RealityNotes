from rest_framework import mixins, viewsets
from .models import Organization, Summary, Experience, Skill, Certification
from .serializers import OrganizationSerializer, SummarySerializer, ExperienceSerializer, SkillSerializer, CertificationSerializer




class OrganizationViewSet(mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class SummaryViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Summary.objects.filter(is_published=True)
    serializer_class = SummarySerializer


class ExperienceViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Experience.objects.filter(is_published=True)
    serializer_class = ExperienceSerializer


class SkillViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CertificationViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = Certification.objects.filter(is_published=True)
    serializer_class = CertificationSerializer
