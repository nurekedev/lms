from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Cateogory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Course(models.Model):
    categories = models.ManyToManyField(Cateogory)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    long_desription = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'https://bulma.io/images/placeholders/1280x960.png'


class Lessons(models.Model):

    DRAFT = 'draft'
    PUBLISHED = 'published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    ARTICLE = 'article'
    QUIZ = 'quiz'
    VIDEO = 'video'

    CHOICES_TYPE_LESSON = (
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
        (VIDEO, 'Video'),
    )


    course = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_desription = models.TextField(blank=True, null=True)
    long_desription = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(
        max_length=20, choices=CHOICES_TYPE_LESSON, default=ARTICLE)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    course = models.ForeignKey(
        Course, related_name='comments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lessons, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)


class Quiz(models.Model):
    lesson = models.ForeignKey(
        Lessons, related_name='quizzes', on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)
