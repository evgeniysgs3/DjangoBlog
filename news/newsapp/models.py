from django.db import models

# Create your models here.


class Articles(models.Model):
    name = models.CharField(max_length=48)
    content = models.TextField()
    publicated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
