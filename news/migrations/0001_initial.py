# Generated by Django 4.1.7 on 2023-03-31 05:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extended_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название новости')),
                ('info', models.CharField(max_length=5000, verbose_name='Описание')),
                ('time_create', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('time_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата измения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото новости')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='extended_user.profile', verbose_name='Организаторы')),
            ],
        ),
    ]