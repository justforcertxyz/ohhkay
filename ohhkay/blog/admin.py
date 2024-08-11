from django.contrib import admin
from .models import Blog
from parler.admin import TranslatableAdmin

admin.site.register(Blog, TranslatableAdmin)