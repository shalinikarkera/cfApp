# Generated by Django 3.0.2 on 2020-05-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0037_image_question_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_question',
            name='option1',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='image_question',
            name='option2',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='image_question',
            name='option3',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='image_question',
            name='option4',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
