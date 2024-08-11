# Generated by Django 5.1 on 2024-08-11 09:47

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blog_html_file_blog_html_file_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.CreateModel(
            name='BlogTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Post Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='blog.blog')),
            ],
            options={
                'verbose_name': 'blog Translation',
                'db_table': 'blog_blog_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]
