from django.db import models
from django.urls import reverse


class Answer(models.Model):
    title = models.CharField('Answer', max_length=50)
    where = models.ForeignKey(
        'Question',
        related_name='Answers',
        on_delete=models.CASCADE
    )
    is_right_answer = models.BooleanField(
        default=False,
        verbose_name='is_right_answer?'
    )

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField('Question', max_length=50)
    quiz = models.ForeignKey(
        'Quiz',
        related_name='Questions',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    for_authenticated_only = models.BooleanField(
        default=False,
        verbose_name='is_for_authenticated_only?'
    )

    def get_absolute_url(self):
        return reverse('quiz', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
