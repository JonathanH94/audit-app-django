from django.urls import path
from . import views

urlpatterns = [path('select_audit', views.select_audit, name='select_audit'),
               path('create_audit/<int:questionnaire_id>', views.create_audit, name='create_audit')
               ]