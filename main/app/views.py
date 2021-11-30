from django.http import HttpResponse

from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *


def main(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            ModelsForm.objects.get_or_create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone']
            )
            messages.success(request, 'Form has been submitted')
            return redirect('/')
        else:
            return HttpResponse("Invalid data")
    else:
        form = Form()
    return render(request, 'app/main.html', {'form': form})

