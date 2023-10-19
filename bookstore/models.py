from django.db import models

# Create your models here.
class book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    inventory=models.IntegerField(null=True)
    
    def __str__(self):
        return self.title