from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from .models import Member

import json
import os

def home(request):
    if request.method == 'POST':
        if "action" in request.POST.keys():
            if request.POST["action"] == "delete":
                return delete(request)
            elif request.POST["action"] == "update":
                return update_or_create(request)
            elif request.POST["action"] == "create":
                return update_or_create(request)
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        members = Member.objects.all()
        for member in members:
            if bool(member.extra) == True:
                member.extra = json.loads(member.extra)
            else:
                member.extra = {}
        context = {'members': members }
        return render(request, 'home.html', context)

def update_or_create(request):
    if request.method == 'POST':
        data = request.POST
        if "fullname" in data.keys() and bool(data['fullname']):
            extra = {}
            for key, value in data.items():
                if key.isnumeric():
                    extra[key] = value

            defaults= {'extra': json.dumps(extra), 'intro': data['intro'] }
            Member.objects.update_or_create(fullname=data['fullname'],
                                            defaults=defaults)
            if 'file' in request.FILES.keys():
                uploaded_file = request.FILES['file']
                filename = uploaded_file.name
                fs = FileSystemStorage()
                # fs.delete(filename)
                filepath = fs.save(filename, uploaded_file)
                uploaded_file_url = fs.url(filepath)
                member = Member.objects.filter(fullname=data['fullname'])[0]
                member.profilename = filepath
                member.save()
            else:
                pass

    else:
            pass
    return HttpResponseRedirect('/')

def delete(request):
    if request.method == 'POST':
        data = request.POST
        if "fullname" in data.keys() and bool(data['fullname']):
            fullname = data['fullname']
            try:
                member = Member.objects.filter(fullname=fullname)[0]
                fs = FileSystemStorage()
                fs.delete(member.profilename)

                member.delete()

            except ObjectDoesNotExist:
                pass
        else:
            pass
    return HttpResponseRedirect('/')
