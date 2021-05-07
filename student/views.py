from django.shortcuts import render
from . forms import StudnetForm
from .models import Student

def Update_products(request, *args, **kwargs):
    form = StudnetForm()
    if request.method=='POST':
        form=StudnetForm(request.POST)
        if form.is_valid():
            
            Student.objects.create(**form.cleaned_data)
        form = StudnetForm()
    context={
        'form':form,
    }
    return render(request, 'rawhtml.html', context)
