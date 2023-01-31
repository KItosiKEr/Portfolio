# Generated by Django 3.2.7 on 2023-01-31 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='logo',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.AlterField(
            model_name='projectscategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.CreateModel(
            name='SendGmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('message', models.TextField()),
                ('phone_number', models.IntegerField(verbose_name='+')),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PortfolioApp.aboutme')),
            ],
        ),
    ]