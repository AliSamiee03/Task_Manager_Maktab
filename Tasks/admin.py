from django.contrib import admin
from .models import Task, Category, Tag

admin.site.register([Task, Tag, Category])

# Register your models here.
