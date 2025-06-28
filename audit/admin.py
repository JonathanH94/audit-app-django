from django.contrib import admin
from .models import Questionnaire, QuestionCategory, Question

# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(QuestionCategory)
admin.site.register(Question)



