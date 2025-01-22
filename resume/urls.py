from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, SummaryViewSet, ExperienceViewSet, SkillViewSet, CertificationViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'summaries', SummaryViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certifications', CertificationViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
]