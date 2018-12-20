from django.shortcuts import render

REQ_DOC_TYPE = "(docType_s:ART OR docType_s:OUV OR docType_s:COUV)"


def index(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "Collection 3SR", "id": "3S-R"}
    publis = requests.get("http://api.archives-ouvertes.fr/search/{}?q={}&sort=producedDate_tdate desc&rows=2000&fl=*".format(structure.get("id"), REQ_DOC_TYPE)).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)


def labo(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "Laboratoire", "id": 706}
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows=100&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE)).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)


def comhet(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "CoMHet", "id": 545341}
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows=100&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE)).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)


def geomecanique(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "Géomécanique", "id": 545340}
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows=100&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE)).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)


def rv(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "RV", "id": 545342}
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=({r} AND authStructId_i:{s})&sort=producedDate_tdate desc&rows=100&fl=*".format(s=structure.get("id"), r=REQ_DOC_TYPE)).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)
