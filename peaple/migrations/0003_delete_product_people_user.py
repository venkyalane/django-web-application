# Generated by Django 4.0.6 on 2024-08-16 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peaple', '0002_people_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='people',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
