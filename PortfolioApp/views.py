from django.shortcuts import render
from rest_framework import permissions
from .models import AboutMe, ProjectsCategory, Project, ProjectImage, Contact, SendGmail
from rest_framework.viewsets import ModelViewSet
from .serializers import (AboutMeSerializers, ProjectsCategorySerializers,
                          ProjectSerializers, ProjectImageSerializers,
                          ContactSerializers, SendGmailSerializers)
from django.contrib.auth import get_user_model


User = get_user_model()


class AboutMeView(ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializers


class ProjectsCategoryView(ModelViewSet):
    queryset = ProjectsCategory.objects.all()
    serializer_class = ProjectsCategorySerializers
    permission_classes = [permissions.IsAdminUser]


class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class ProjectImageView(ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class SendGmailView(ModelViewSet):
    queryset = SendGmail.objects.all()
    serializer_class = SendGmailSerializers
# Create your views here.
