# Generated by Django 4.0.6 on 2022-08-16 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_student_mobile_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='mobile_no',
        ),
    ]