# Generated by Django 2.1.2 on 2018-10-26 15:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0005_auto_20181026_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='downvotes',
            field=models.ManyToManyField(blank=True, default=0, related_name='downvotes_t', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issues',
            name='upvotes',
            field=models.ManyToManyField(blank=True, default=0, related_name='upvotes_t', to=settings.AUTH_USER_MODEL),
        ),
    ]
