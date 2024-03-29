# Generated by Django 4.1.7 on 2023-09-03 17:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extended_user', '0002_alter_profile_photo'),
        ('event', '0003_alter_event_organizers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название занятия')),
                ('info', models.CharField(max_length=5000, verbose_name='Описание')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('time_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date_soft', models.DateField(blank=True, null=True, verbose_name='Мягкий дедлайн')),
                ('end_date_hard', models.DateField(blank=True, null=True, verbose_name='Жесткий дедлайн')),
                ('file', models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Прикрепленный файл')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='classes_by_event', to='event.event', verbose_name='Мероприятие')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='teacher', to='extended_user.profile', verbose_name='Преподаватель')),
            ],
        ),
    ]
