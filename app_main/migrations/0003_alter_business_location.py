# Generated by Django 4.0.3 on 2022-03-21 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_neighbourhood_neighbour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='app_main.location'),
        ),
    ]
