from django.shortcuts import render, redirect, get_object_or_404
from .models import Response, ResponseAnswer, Question, Questionnaire
from .forms import AuditForm
from django.contrib import messages

# Create your views here.

"""
####################
#SELECT AUDIT FROM PANEL LIST OF AUDITS
####################
"""
def select_audit(request):
    if request.method == 'GET':
        questionnaires = Questionnaire.objects.all()

        return render(request, 'select_audit.html', {'questionnaires': questionnaires})

"""
####################
#CREATE AUDIT
####################
"""
def create_audit(request, questionnaire_id):
    if request.method == 'GET':
        questionnaire_result = Questionnaire.objects.get(pk=questionnaire_id)

        form = AuditForm(questionnaire=questionnaire_result)

        return render(request, 'create_audit.html', {'form': form})

    elif request.method == 'POST':

        questionnaire_result = Questionnaire.objects.get(pk=questionnaire_id)

        form = AuditForm( request.POST, questionnaire=questionnaire_result)
        if form.is_valid():
          team = form.cleaned_data['team']
          user = request.user
          completed_date = form.cleaned_data['completed_date']

          response = Response.objects.create(questionnaire=questionnaire_result, user=user, team=team,completed_date=completed_date)
          for key, value in form.cleaned_data.items():
             if key.startswith('question_'):
                 question_id = int(key.split('_')[1])
                 answer = form.cleaned_data[key]
                 question = Question.objects.get(pk=question_id)
                 ResponseAnswer.objects.create(response=response, question=question, answer=answer)
          messages.success(request, "Successfully created audit")
        return  render(request, 'confirmation.html')


"""
####################
#MY SUBMISSIONS
####################
"""

def my_submissions(request):
    if request.method == 'GET':
        response = Response.objects.filter(user=request.user)

    return  render(request, 'my_submissions.html', {'response': response})


"""
####################
#VIEW SUBMISSION
####################
"""

def view_submission(request, response_id):
    if request.method == 'GET':
        response_answer = ResponseAnswer.objects.filter(response_id=response_id)

        return render(request, 'view_submission.html', {'response_answer': response_answer})

"""
####################
#DELETE SUBMISSION
####################
"""
def delete_submission(request, response_id):
    if request.method == 'POST':
        response = get_object_or_404(Response, pk=response_id)
        response.delete()

        messages.success(request, "Successfully deleted submission")
        return redirect('my_submissions')

"""
####################
#EDIT SUBMISSION
####################
"""
def edit_submission(request, response_id):
    if request.method == 'GET':
        response = Response.objects.get(pk=response_id)

        questionnaire = response.questionnaire

        response_answer = ResponseAnswer.objects.filter(response_id=response_id)



        initial_data = {
            'team': response.team,
            'completed_date': response.completed_date,



        }

        for ans in response_answer:
            key = f"question_{ans.question.id}"
            value = ans.answer
            initial_data[key] = value

        form = AuditForm(initial=initial_data, questionnaire=questionnaire)


        return render(request, 'edit_submission.html', {'edit_form': form})
    elif request.method == 'POST':

        response = Response.objects.get(pk=response_id)

        questionnaire = response.questionnaire

        form = AuditForm(request.POST, questionnaire=questionnaire)

        if form.is_valid():
            new_team = form.cleaned_data['team']
            response.team  = new_team
            response.save()

            for key, value in form.cleaned_data.items():
                if key.startswith('question_'):
                    question_id = int(key.split('_')[1])
                    answer = form.cleaned_data[key]
                    question = Question.objects.get(pk=question_id)
                    ResponseAnswer.objects.update_or_create(response=response, question=question, defaults={'answer':answer})
        messages.success(request, "Audit was updated")
        return redirect('my_submissions')




