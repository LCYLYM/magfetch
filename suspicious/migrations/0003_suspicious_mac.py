# Generated by Django 2.1.7 on 2019-04-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suspicious', '0002_suspicious_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='suspicious',
            name='mac',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='mac address'),
        ),
    ]
