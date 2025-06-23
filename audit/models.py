from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget


# Create your models here.

class Questionnaire(models.Model):
    audit_title = models.CharField(max_length=50)
    audit_description = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.audit_title


class QuestionCategory(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    category_title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    order_index = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_title



class Question(models.Model):
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=250)
    question_type = models.CharField(max_length=50)
    order_index = models.IntegerField()
    is_required = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_title

# class QuestionAnswer(models.Model):
#     question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=50)
#     order_index = models.IntegerField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name


class Response(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    completed_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.questionnaire.audit_title}"

class ResponseAnswer(models.Model):
    QUESTION_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('na', 'N/A')
    )
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3, choices=QUESTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question.question_title} - {self.answer}"










