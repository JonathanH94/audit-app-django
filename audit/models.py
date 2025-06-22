from django.db import models

# Create your models here.

class Questionnaire(models.Model):
    audit_title = models.CharField(max_length=50)
    audit_description = models.CharField(max_length=150)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class QuestionCategory(models.Model):
    Questionnaire_id = models.ForeignKey(Questionnaire, on_delete=models.PROTECT)
    category_title = models.CharField(max_length=50)
    order_index = models.IntegerField()
    is_required = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Question(models.Model):
    Question_category_id = models.ForeignKey(QuestionCategory, on_delete=models.PROTECT)




