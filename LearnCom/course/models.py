from django.db import models

# Create your models here.
class Cateogory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    categories = models.ManyToManyField(Cateogory)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    long_desription = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title