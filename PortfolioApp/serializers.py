from .models import AboutMe, ProjectsCategory, Project, ProjectImage, Contact, SendGmail
from rest_framework.serializers import ModelSerializer

class AboutMeSerializers(ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'


class ProjectsCategorySerializers(ModelSerializer):
    class Meta:
        model = ProjectsCategory
        fields = '__all__'


class ProjectSerializers(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageSerializers(ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ContactSerializers(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class SendGmailSerializers(ModelSerializer):
    class Meta:
        model = SendGmail
        fields = '__all__'
        