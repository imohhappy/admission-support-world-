# Generated by Django 4.0.6 on 2022-08-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_rename_countrys_teacher_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobile_no',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]