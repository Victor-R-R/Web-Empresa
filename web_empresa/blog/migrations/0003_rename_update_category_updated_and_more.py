# Generated by Django 4.2.1 on 2023-06-12 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]
