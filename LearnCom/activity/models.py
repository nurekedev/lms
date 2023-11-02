from django.db import models
from django.contrib.auth.models import User
from course.models import Course, Lessons

# Create your models here.

class Activity(models.Model):
    STARTED = 'started'
    DONE = 'done'

    STATUS_CHOISES = (
        (STARTED, 'Started'),
        (DONE, 'Done'),
    )


    course = models.ForeignKey(Course, related_name='activities', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lessons, related_name='activities', on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default=STARTED)
    created_by = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_by} - {self.course.title}"
