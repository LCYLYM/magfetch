# Generated by Django 2.1.7 on 2019-02-20 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=20, null=True, verbose_name='category')),
                ('identifier', models.CharField(blank=True, max_length=200, null=True, verbose_name='identifier')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('subject', models.CharField(blank=True, max_length=100, null=True, verbose_name='subject')),
                ('message', models.TextField(blank=True, max_length=500, null=True, verbose_name='message')),
                ('has_read', models.BooleanField(default=False, verbose_name='has read')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to='accounts.UserProfile', verbose_name='receiver')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to='accounts.UserProfile', verbose_name='sender')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
                'ordering': ['-updated_at'],
            },
        ),
    ]
