# Generated by Django 3.2.7 on 2023-01-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0008_alter_sendgmail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendgmail',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
