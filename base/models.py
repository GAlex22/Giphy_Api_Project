from django.db import models

# Create your models here.

class Search(models.Model):
    search_term = models.CharField(max_length=50)
    response = models.TextField()
    
    def __str__(self):
        return self.search_term
