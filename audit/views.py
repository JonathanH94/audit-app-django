from django.shortcuts import render
from .models import Response
from .forms import AuditForm

# Create your views here.




def create_audit(request):
    if request.method == 'POST':
        form = AuditForm(request.POST)
        if form.is_valid():
            print(form.fields)

