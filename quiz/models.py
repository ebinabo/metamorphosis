from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AbstractQuestion(models.Model):
    question_number = models.IntegerField()
    question = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.question


class BooleanQuestion(AbstractQuestion):
    pass

class TheoryQuestion(AbstractQuestion):
    pass


class BooleanQuestionAnswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='boolean_questions'
    )
    question = models.ForeignKey(
        BooleanQuestion,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    answer = models.BooleanField()

class TheoryQuestionAnswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='theory_questions'
    )
    question = models.ForeignKey(
        TheoryQuestion,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    answer = models.TextField()


class MultipleChoiceQuestionOption(models.Model):
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option


class MultipleChoiceQuestion(AbstractQuestion):
    options = models.ManyToManyField(
        MultipleChoiceQuestionOption,
        related_name='options'
    )


class MultipleChoiceQuestionAnswer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='multiple_choice_questions'
    )
    question = models.ForeignKey(
        MultipleChoiceQuestion,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    answer = models.ForeignKey(
        MultipleChoiceQuestionOption,
        on_delete=models.CASCADE,
        related_name='answers'
    )