# Generated by Django 4.0.3 on 2022-03-22 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mtaa', to='app_main.location'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='neighbour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='live', to='app_main.neighbourhood'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]