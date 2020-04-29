# Generated by Django 3.0.2 on 2020-04-28 14:10

from django.db import migrations, models
import user_admin.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0028_entity_status_enitity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity_status',
            name='description',
            field=models.CharField(max_length=100, validators=[user_admin.models.validate_not_spaces]),
        ),
    ]
