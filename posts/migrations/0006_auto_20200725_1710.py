# Generated by Django 3.0.5 on 2020-07-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='category',
        ),
    ]
