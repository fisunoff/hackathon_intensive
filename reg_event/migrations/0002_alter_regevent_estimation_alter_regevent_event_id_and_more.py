# Generated by Django 4.1.7 on 2023-09-03 17:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extended_user', '0002_alter_profile_photo'),
        ('event', '0003_alter_event_organizers'),
        ('reg_event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regevent',
            name='estimation',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка работы студента'),
        ),
        migrations.AlterField(
            model_name='regevent',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='regs_by_event', to='event.event', verbose_name='Мероприятие'),
        ),
        migrations.AlterField(
            model_name='regevent',
            name='intern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='regs_by_student', to='extended_user.profile', verbose_name='Студент'),
        ),
        migrations.AlterField(
            model_name='regevent',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Обратная связь'),
        ),
    ]