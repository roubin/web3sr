from django.shortcuts import render

import requests
from time import strftime
from time import gmtime

REQ_DOC_TYPE = "(docType_s:ART OR docType_s:OUV OR docType_s:COUV)"

N_PUBLI_MAX = 100


def index(request):
    structure = {"name": "Collection 3SR", "id": "3S-R"}
    req = "http://api.archives-ouvertes.fr/search/{}?q={}&sort=producedDate_tdate desc&rows={}&fl=*".format(structure.get("id"), REQ_DOC_TYPE, N_PUBLI_MAX)
    print(req)
    publis = requests.get(req).json()
    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "npublis": N_PUBLI_MAX,
               "structure": structure}
    return render(request, 'publi.html', context)


def labo(request):
    structure = {"name": "Laboratoire", "id": 706}
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX)
    print(req)
    publis = requests.get(req).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "npublis": N_PUBLI_MAX,
               "structure": structure}
    return render(request, 'publi.html', context)


def comhet(request):
    structure = {"name": "CoMHet", "id": 545341}
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX)
    print(req)
    publis = requests.get(req).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "npublis": N_PUBLI_MAX,
               "structure": structure}
    return render(request, 'publi.html', context)


def geomecanique(request):
    structure = {"name": "Géomécanique", "id": 545340}
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX)
    print(req)
    publis = requests.get(req).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "npublis": N_PUBLI_MAX,
               "structure": structure}
    return render(request, 'publi.html', context)


def rv(request):
    structure = {"name": "RV", "id": 545342}
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX)
    print(req)
    publis = requests.get(req).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "npublis": N_PUBLI_MAX,
               "structure": structure}
    return render(request, 'publi.html', context)
