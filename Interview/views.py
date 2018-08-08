from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import FileResponse


def home(request):
    return render(request, 'interview.html')


def download(request, cv_id):
    return FileResponse(open('res/徐智涛 1年.pdf', 'rb'))
