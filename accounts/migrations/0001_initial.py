# Generated by Django 2.1.7 on 2019-02-12 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.PositiveSmallIntegerField(choices=[(0, 'INFORMATION TECHNOLOGY'), (1, 'COMPUTER SCIENCE & ENGINEERING'), (2, 'ELECTRICAL & ELECTRONIC ENGINEERING'), (3, 'MECHANICAL ENGINEERING'), (4, 'APPLIED PHYSICS'), (5, 'APPLIED CHEMESTRY'), (6, 'ARCHITECTURE'), (7, 'TEXTILE ENGINEERING')], verbose_name='faculty')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('user_role', models.PositiveSmallIntegerField(choices=[(0, 'Marketing Manager'), (1, 'Administrator'), (2, 'Marketing Coordinator'), (3, 'Faculty Guest'), (4, 'Student')], default=4, verbose_name='user role')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_faculty', to='accounts.Faculty', verbose_name='faculty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-user__date_joined'],
            },
        ),
    ]