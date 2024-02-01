# Generated by Django 4.2 on 2024-02-01 21:27

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('url_hash', models.SlugField(default='', help_text='Unique URL path for the Article', max_length=5, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', help_text='Title of the Article', max_length=1000)),
                ('description', models.TextField(default='', max_length=1000)),
                ('image', models.ImageField(default='', upload_to='assets/article')),
                ('image_alt', models.CharField(default='', max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_featured', models.BooleanField(default=False, help_text='Featured Article? (Will display as first Article on Homepage)')),
                ('published_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('title', 'published_at', 'url_hash'),
            },
        ),
    ]
