# Generated by Django 3.1 on 2020-11-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('seobird657', '0009_remove_recipebirdpage_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssbirdpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
