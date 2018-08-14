from django.template import loader
from django.shortcuts import render
from django.http import FileResponse
import json
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def home(request):
    path = os.path.abspath('.')
    f = open(path + "/res/db.json", encoding='utf-8')
    db = json.load(f)

    template = loader.get_template('home.html')

    # candidates = db['candidates']
    # print(candidates)

    return HttpResponse(template.render(db, request))


def interview(request, cv_id):
    path = os.path.abspath('.')
    f = open(path + "/res/db.json", encoding='utf-8')
    db = json.load(f)
    candidates = db['candidates']
    for candidate in candidates:
        if candidate['id'] == cv_id:
            template = loader.get_template('interview.html')
            return HttpResponse(template.render({"candidate": candidate}, request))
    return render(request, 'error.html')


def download(request, cv_id):
    filename = 'res/' + str(cv_id) + '.pdf'
    return FileResponse(open(filename, 'rb'))


def submit(request, cv_id):
    comm1 = request.POST['c1']
    comm2 = request.POST['c2']
    comm3 = request.POST['c3']

    path = os.path.abspath('.')
    f = open(path + "/res/db.json", encoding='utf-8')
    db = json.load(f)
    candidates = db['candidates']
    for i in range(len(candidates)):
        if candidates[i]['id'] == cv_id:
            candidates[i]['comment1'] = comm1
            candidates[i]['comment2'] = comm2
            candidates[i]['comment3'] = comm3
            break

    with open(path + "/res/db.json", 'w') as fw:
        json.dump({'candidates': candidates}, fw, indent=2)

    return HttpResponseRedirect(reverse('home'))
