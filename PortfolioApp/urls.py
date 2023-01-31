from rest_framework.routers import DefaultRouter as DR
from PortfolioApp.views import (AboutMeView, ProjectsCategoryView, 
                                ProjectView, ProjectImageView,
                                ContactView, SendGmailView)
from django.urls import include

router = DR()

router.register('aboutme', AboutMeView, basename='aboutme')
router.register('projects_category', ProjectsCategoryView, basename='projects_category')
router.register('project', ProjectView, basename='project')
router.register('project_image', ProjectImageView, basename='project_image')
router.register('contact', ContactView, basename='contact')
router.register('send_gmail', SendGmailView, basename='send_gmail')


urlpatterns = []

urlpatterns += router.urls