# Generated by Django 3.0.2 on 2020-04-14 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0010_auto_20200408_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='center',
            name='center_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='entity_status',
            name='description',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='entity_type',
            name='description',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='module_level',
            name='level_description',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='module_level',
            name='level_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='program_module',
            name='module_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='program_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
