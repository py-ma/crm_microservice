from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from project.main import linkmaker
from linkmaker import *

# from ..main.linkmaker import get_response


def main(request):
    form_name = ''
    form_email = ''
    form_phone = ''
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
            # create a contact form
            # contact = [form['name'], form['email'], form['phone']]
            # create a...
            form_name = form.cleaned_data.get("name")
            form_email = form.cleaned_data.get("email")
            form_phone = form.cleaned_data.get("phone")

            contact = {'form': form, 'name': form_name,
                   'lastname': form_email, 'phone': form_phone}

            return render(request, contact)
        else:
            return HttpResponse("Invalid data")
    else:
        form = Form()
        return render(request, 'app/main.html', {'form': form})
'''
def get_contact(request):
    if request.method == "GET":
        if get_response.status_code == "200":
            messages.success(request, 'Successful search')
            # return redirect('/')
        else:
            return HttpResponse("Invalid data")
    else:
        pass
        # add contact using request.method post with "https://login.amocrm.ru/api/v4/contacts"
'''
