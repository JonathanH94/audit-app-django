from django import forms
from .models import Team


QUESTION_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
    ('na', 'N/A'),
]

class AuditForm(forms.Form):

    def __init__(self, *args, questionnaire=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.questionnaire = questionnaire
        self.fields['user'] = forms.CharField(widget=forms.HiddenInput)
        self.fields['team'] = forms.ModelChoiceField(queryset=Team.objects.all())
        self.fields['completed_date'] = forms.DateTimeField()

        for category in questionnaire.questioncategory_set.all():
               for question in category.question_set.all():
                   self.fields[f'question_{question.id}'] =forms.ChoiceField(choices=QUESTION_CHOICES,
                                                                             widget=forms.RadioSelect,
                                                                             label=question.question_title,
                                                                             required=question.is_required)



