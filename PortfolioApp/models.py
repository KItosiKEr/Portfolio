from django.db import models
from django import forms


class AboutMe(models.Model):
    user = models.TextField()
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    biography = models.TextField()
    photo = models.ImageField(upload_to='Image', blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='projects',null=True, )

    def __str__(self):
        return self.user


class ProjectsCategory(models.Model):
    title = models.CharField(max_length=127)
    pre_description = models.TextField()
    descritipon = models.TextField()
    image = models.ImageField(upload_to='Image', blank=True)


class Project(models.Model):
    user = models.ForeignKey(AboutMe, blank=True, on_delete=models.CASCADE, related_name='projects', null=True, )
    category = models.TextField()
    project_name = models.CharField(max_length=127)
    pre_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='Image', blank=True)
    link = models.URLField(max_length=200)
    created_date = models.DateTimeField(blank=True, null=True, verbose_name='когда',auto_now_add=True)


    # def __str__(self):
    #     return self.user

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE  )
    image = models.ImageField(upload_to='Image',blank=True)


class Contact(models.Model):
    user = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    logo = models. ImageField(upload_to='Image',blank=True)
    link = models.URLField(max_length=200)
    name = models.CharField(max_length=127)


class SendGmail(models.Model):
    user = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(max_length=255, unique=True)
    message = models.TextField()
    phone_number = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.first_name


# Create your models here.
