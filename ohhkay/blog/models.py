from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField("Post Title", max_length=50, unique=True)
    pub_date = models.DateTimeField("Date Published", default=timezone.now)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    html_file = models.FileField("HTML File",
        upload_to=f"blog/templates/blog/entries/",
        null=True, blank=True
    )

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def template_path(self):
        return self.html_file.name.split("templates/")[1]