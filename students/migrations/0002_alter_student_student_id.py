# Generated by Django 4.0.6 on 2024-08-12 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stid', to='students.studentid'),
        ),
    ]