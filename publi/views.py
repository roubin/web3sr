from django.shortcuts import render

import requests
from time import strftime
from time import gmtime

REQ_DOC_TYPE = "(docType_s:ART OR docType_s:OUV OR docType_s:COUV)"
BRIDGE_TYPES = {"ART": "Articles", "COMM": "Conferences", "COUV": "Books", "THESE": "These"}
SORT_BY = "producedDate_s"  # "journalDate_s"
N_PUBLI_MAX = 1000


def index(request):
    structure = {"name": "Collection 3SR", "id": "3S-R"}
    req = "http://api.archives-ouvertes.fr/search/{}?q={}&sort={} desc&rows={}&fl=*".format(structure.get("id"), REQ_DOC_TYPE, SORT_BY, N_PUBLI_MAX)
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
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort={so} desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX, so=SORT_BY)
    print(req)
    publis = requests.get(req).json()

    req = "https://api.archives-ouvertes.fr/ref/author/?q=structureId_i:706"
    print(req)
    authors = requests.get(req).json()
    print(authors)

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
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort={so} desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX, so=SORT_BY)
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
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort={so} desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX, so=SORT_BY)
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
    req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort={so} desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX, so=SORT_BY)
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


def idHal(request):
    idHal = request.GET.get('q', False)
    print("idHal: {}".format(idHal))
    author = {"idHal": idHal}
    # req = "http://api.archives-ouvertes.fr/search/?q=({r} AND authIdHal_s:{s})&sort={so} desc&rows={n}&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE, n=N_PUBLI_MAX, so=SORT_BY)
    req = "http://api.archives-ouvertes.fr/search/?q=(authIdHal_s:{s})&sort={so} desc&rows={n}&fl=*".format(s=author.get("idHal"), n=N_PUBLI_MAX, so=SORT_BY)
    print(req)
    publis_by_type = dict()
    api_error = dict()
    publis = requests.get(req).json()
    if 'error' in publis:
        api_error = publis['error']
    else:
        publis = publis["response"]["docs"]
        req_author = 'https://api.archives-ouvertes.fr/ref/author/?q=idHal_s:{s}'.format(s=author.get("idHal"))
        print(req_author)
        idhal_info = requests.get(req_author).json()
        author["docid"] = idhal_info.get("response")["docs"]
        for i, publi in enumerate(publis):
            print(i, publi["citationFull_s"])
            type = BRIDGE_TYPES.get(publi.get("docType_s")) if BRIDGE_TYPES.get(publi.get("docType_s")) is not None else publi.get("docType_s")
            if type in publis_by_type:
                publis_by_type[type].append(publi)
            else:
                publis_by_type[type] = [publi]

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis_by_type": publis_by_type,
               "date": date,
               "author": author,
               "error": api_error}
    return render(request, 'idHal.html', context)
