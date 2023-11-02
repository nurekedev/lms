# Generated by Django 4.2.6 on 2023-11-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_quiz_delete_quizmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_type',
            field=models.CharField(choices=[('article', 'Article'), ('quiz', 'Quiz'), ('video', 'Video')], default='article', max_length=20),
        ),
    ]