# Generated by Django 3.0 on 2020-06-29 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seobird657', '0004_seosettings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlebirdpage',
            old_name='article',
            new_name='body',
        ),
    ]
