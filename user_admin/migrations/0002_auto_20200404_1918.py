# Generated by Django 3.0.2 on 2020-04-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('batch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('sessions_count', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('batch_incharge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.facilitator')),
            ],
        ),
        migrations.CreateModel(
            name='module_level',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('level_number', models.IntegerField()),
                ('level_description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='center',
            name='center_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.entity_type'),
        ),
        migrations.CreateModel(
            name='student_module_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
                ('student_student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.student')),
            ],
        ),
        migrations.CreateModel(
            name='student_batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.batch')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.student')),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
                ('answer', models.CharField(blank=True, max_length=500, null=True)),
                ('question_type', models.CharField(blank=True, max_length=100, null=True)),
                ('narrative', models.CharField(blank=True, max_length=100, null=True)),
                ('option1', models.CharField(blank=True, max_length=100, null=True)),
                ('option2', models.CharField(blank=True, max_length=100, null=True)),
                ('option3', models.CharField(blank=True, max_length=100, null=True)),
                ('option4', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=100, null=True)),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.module_level')),
            ],
        ),
        migrations.CreateModel(
            name='program_module',
            fields=[
                ('module_id', models.IntegerField(primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=100)),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program')),
            ],
        ),
        migrations.AddField(
            model_name='module_level',
            name='module_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program_module'),
        ),
        migrations.AddField(
            model_name='batch',
            name='center_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.center'),
        ),
        migrations.AddField(
            model_name='batch',
            name='program_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.program'),
        ),
        migrations.AddField(
            model_name='batch',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_admin.entity_status'),
        ),
    ]