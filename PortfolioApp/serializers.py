from .models import AboutMe, ProjectsCategory, Project, ProjectImage, Contact, SendGmail
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, exceptions

# class AboutMeSerializers(ModelSerializer):
#     project = ProjectSerializers(many=True, read_only=True)
#     class Meta:
#         model = AboutMe
#         fields = '__all__'


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



class AboutMeSerializers(ModelSerializer):
    # project1 = ProjectSerializers(many=True, read_only=True)
    class Meta:
        model = AboutMe
        fields = 'id','user', 'first_name', 'last_name', 'biography', 'photo', 'projects_p',
    

class AboutMeDetailSerializers(ModelSerializer):
    projects = ProjectSerializers(many=True, read_only=True)
    class Meta:
        model = AboutMe
        fields = 'id','user', 'first_name', 'last_name', 'biography', 'photo', 'projects', 


# class RegistrationSerializer(serializers.Serializer):
#     username= serializers.CharField()
#     password= serializers.CharField()
#     email= serializers.CharField()
#     def validate_password(self,value):
#         if len(value) <8:
#             raise exceptions.ValidationError('Password is too short')
#         elif len (value) >24:
#             raise exceptions.ValidationError ('Password is too long')
#         return value