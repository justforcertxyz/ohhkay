# Generated by Django 5.1 on 2024-08-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_text_blog_html_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='html_content',
        ),
        migrations.AddField(
            model_name='blog',
            name='html_file',
            field=models.FileField(blank=True, null=True, upload_to='blog/templates/blog/entries/', verbose_name='HTML File'),
        ),
    ]
