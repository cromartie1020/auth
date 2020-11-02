from django.db import models

# Create your models here.
class Example(models.Model):
    name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    text=models.TextField(default="Nothing Enter yet.")
    def __str__(self):
        return self.name

        