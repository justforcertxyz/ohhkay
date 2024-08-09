from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField("Post Title", max_length=50, unique=True)
    pub_date = models.DateTimeField("Date Published", default=timezone.now)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    text = models.TextField("Blog Text", max_length=6000, default="")

    tags = TaggableManager()

    def __str__(self):
        return self.title