from django.db import models

class Task(models.Model):
    Title = models.CharField(max_length = 100)
    Description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    