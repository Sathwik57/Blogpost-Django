# Generated by Django 3.2.9 on 2021-11-09 12:14

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_blog_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelManagers(
            name='blog',
            managers=[
                ('related', django.db.models.manager.Manager()),
            ],
        ),
    ]
