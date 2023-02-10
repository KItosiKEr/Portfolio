from django.shortcuts import render
from rest_framework import permissions
from .models import AboutMe, ProjectsCategory, Project, ProjectImage, Contact, SendGmail
from rest_framework.viewsets import ModelViewSet
from .serializers import (AboutMeSerializers, ProjectsCategorySerializers,
                          ProjectSerializers, ProjectImageSerializers,
                          ContactSerializers, SendGmailSerializers)
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

User = get_user_model()


class ProjectViewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 6


class AboutMeView(ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializers
    filter_backends=(
        DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter
    )
    # filterset_fields=(
    #     'date_of_issue',
    # )
    search_fields=(
        'first_name', 'last_name',
    )
    ordering_fields=(
        'id',
    )
    # user = AboutMe.objects.get(id=1)
    # Project.objects.filter(author=user)

    @action(methods=['post',],detail=True,serializer_class=ProjectSerializers,permission_classes=(permissions.IsAuthenticatedOrReadOnly,))
    def add_project(self ,request, *args,**kwargs):
        aboutme = self.get_object()
        user = request.user
        serializer=ProjectSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        project=Project.objects.create(
            aboutme=aboutme,
            author=user,
            user= data.get('user'),
            category=data.get('category'),
            project_name=data.get('project_name'),
            pre_description =data.get('pre_description '),
            description=data.get('description'),
            image=data.get('image'),
            link=data.get('link'),
        
        
        )
        return Response(ProjectSerializers(project).data)

class ProjectsCategoryView(ModelViewSet):
    queryset = ProjectsCategory.objects.all()
    serializer_class = ProjectsCategorySerializers
    permission_classes = [permissions.IsAdminUser]


class ProjectView(ModelViewSet):
    queryset = Project.objects.order_by('-created_date').all()
    serializer_class = ProjectSerializers
    pagination_class = ProjectViewPagination


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
