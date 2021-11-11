# Generated by Django 3.2.9 on 2021-11-08 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211108_1943'),
        ('blogs', '0005_blog_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
