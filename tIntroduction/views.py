from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import Member

import json
import os

def home(request):
    return render(request, "index.html", {})

def get_intro(request):
    context = []
    members = Member.objects.all()
    for member in members:
        info = {"id": member.identifier, "name": member.fullname,
                "attr": [], "profilename": member.profilename}
        if bool(member.extra) == True:
            attributes = json.loads(member.extra)
            for key, value in attributes.items():
                info["attr"].append({"attr": key, "cont": value})
        context.append(info)
    return JsonResponse(context, safe=False)
