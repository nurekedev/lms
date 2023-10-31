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


class Lessons(models.Model):

    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'

    CHOICES_TYPE_LESSON = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz')
    )

    course = models.ForeignKey(Course, related_name='lessons',on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    long_desription = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(max_length=20, choices=CHOICES_TYPE_LESSON, default=ARTICLE)