# Generated by Django 5.1.2 on 2024-10-15 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsappbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='phone_number',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]