# Generated by Django 3.2.7 on 2023-02-06 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0002_auto_20230206_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='PortfolioApp.aboutme'),
        ),
    ]