# Generated by Django 3.0.2 on 2020-04-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0007_batch_partner_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='student_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]