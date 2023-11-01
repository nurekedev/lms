# Generated by Django 4.2.6 on 2023-11-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_cateogory_options_quizmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('answer', models.CharField(max_length=200, null=True)),
                ('option1', models.CharField(max_length=200, null=True)),
                ('option2', models.CharField(max_length=200, null=True)),
                ('option3', models.CharField(max_length=200, null=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='course.lessons')),
            ],
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]
