from django.urls import path
from . import views

urlpatterns = [path('select_audit', views.select_audit, name='select_audit'),
               path('create_audit/<int:questionnaire_id>', views.create_audit, name='create_audit'),
               path('my_submissions', views.my_submissions, name='my_submissions'),
               path('view_submission/<int:response_id>', views.view_submission, name='view_submission')
               ]