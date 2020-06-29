# Generated by Django 3.0 on 2020-06-29 20:04

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('seobird657', '0005_auto_20200629_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipebirdpage',
            name='body',
            field=wagtail.core.fields.StreamField([('recipe', wagtail.core.blocks.StructBlock([('ingredients', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('ingredient', wagtail.core.blocks.CharBlock()), ('amount', wagtail.core.blocks.CharBlock(required=False))]))), ('instructions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))], null=True, required=False))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipebirdpage',
            name='recipe',
            field=wagtail.core.fields.StreamField([('ingredients', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('ingredient', wagtail.core.blocks.CharBlock()), ('amount', wagtail.core.blocks.CharBlock(required=False))]))), ('instructions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))], blank=True, null=True),
        ),
    ]
