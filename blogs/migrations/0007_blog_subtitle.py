# Generated by Django 3.2.9 on 2021-11-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blog_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
