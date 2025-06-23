from django.shortcuts import render
from .models import Response
from .forms import AuditForm
from.models import Questionnaire

# Create your views here.

#SELECT AUDIT FROM PANEL LIST OF AUDITS
def select_audit(request):
    if request.method == 'GET':
        questionnaires = Questionnaire.objects.all()

        return render(request, 'select_audit.html', {'questionnaires': questionnaires})



#CREATE AUDIT

def create_audit(request, questionnaire_id):
    if request.method == 'GET':
        questionnaire_result = Questionnaire.objects.get(pk=questionnaire_id)

        form = AuditForm(questionnaire=questionnaire_result)

        return render(request, 'create_audit.html', {'form': form})

    elif request.method == 'POST':
        return 'PLACEHOLDER: SUBMIT LOGIC'


#Submit audit once created