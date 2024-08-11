from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from parler.models import TranslatableModel, TranslatedFields

class Blog(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Post Title", max_length=50, unique=True),
        slug = models.SlugField("Slug", max_length=50, unique=True),
    )

    pub_date = models.DateTimeField("Date Published", default=timezone.now)
    html_file_de = models.FileField("HTML File German",
        upload_to=f"blog/templates/blog/entries/",
        null=True, blank=True
    )
    html_file_en = models.FileField("HTML File English",
        upload_to=f"blog/templates/blog/entries/",
        null=True, blank=True
    )

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def template_path_de(self):
        return self.html_file_de.name.split("templates/")[1]

    def template_path_en(self):
        return self.html_file_en.name.split("templates/")[1]