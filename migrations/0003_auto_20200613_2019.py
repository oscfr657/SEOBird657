# Generated by Django 3.0 on 2020-06-13 18:19

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('seobird657', '0002_auto_20200613_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBirdPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('intro', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('show_breadcrumbs', models.BooleanField(default=False)),
                ('show_coverImage', models.BooleanField(default=False)),
                ('show_date', models.BooleanField(default=False)),
                ('exclude_from_sitemap', models.BooleanField(default=False)),
                ('article', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'superscript', 'subscript', 'strikethrough', 'ol', 'ul', 'hr', 'link', 'document-link', 'blockquote', 'embed', 'image'], null=True, required=False)), ('media', wagtail.core.blocks.StructBlock([('muted', wagtail.core.blocks.BooleanBlock(default=True, help_text='Muted', required=False)), ('autoplay', wagtail.core.blocks.BooleanBlock(default=False, help_text='Autoplay', required=False)), ('loop', wagtail.core.blocks.BooleanBlock(default=False, help_text='Loop', required=False)), ('controls', wagtail.core.blocks.BooleanBlock(default=True, help_text='Controls', required=False)), ('block_media', wagtailmedia.blocks.AbstractMediaChooserBlock())], null=True, required=False)), ('code', wagtail.core.blocks.StructBlock([('code', wagtail.core.blocks.TextBlock(required=True))], null=True, required=False)), ('html', wagtail.core.blocks.StructBlock([('html', wagtail.core.blocks.RawHTMLBlock())], null=True, required=False))], blank=True, null=True)),
                ('cover_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ArticleBirdPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='seobird657.ArticleBirdPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seobird657_articlebirdpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='articlebirdpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='seobird657.ArticleBirdPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
