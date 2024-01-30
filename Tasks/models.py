from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length= 100)
    creator = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    due_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    