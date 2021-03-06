# Generated by Django 3.0.2 on 2020-04-19 13:13

from django.db import migrations, models
import user_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0018_auto_20200418_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity_status',
            name='description',
            field=models.CharField(max_length=100, unique=True, validators=[user_admin.models.validate_not_spaces]),
        ),
        migrations.AlterField(
            model_name='entity_type',
            name='description',
            field=models.CharField(max_length=100, unique=True, validators=[user_admin.models.validate_not_spaces]),
        ),
        migrations.AlterField(
            model_name='module_level',
            name='level_description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, validators=[user_admin.models.validate_not_spaces]),
        ),
    ]
