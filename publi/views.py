from django.shortcuts import render


def index(request):
    import requests
    from time import strftime
    from time import gmtime

    publis = requests.get('http://api.archives-ouvertes.fr/search/3S-R?q=(docType_s:ART)&sort=producedDate_tdate desc&rows=100&fl=*').json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date}
    return render(request, 'publi.html', context)


def labo(request):
    import requests
    from time import strftime
    from time import gmtime

    structure = {"name": "Laboratoire", "id": 706}
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=(docType_s:ART AND authStructId_i:{})&sort=producedDate_tdate desc&rows=100&fl=*".format(structure.get("id"))).json()

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
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=(docType_s:ART AND authStructId_i:{})&sort=producedDate_tdate desc&rows=100&fl=*".format(structure.get("id"))).json()

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
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=(docType_s:ART AND authStructId_i:{})&sort=producedDate_tdate desc&rows=100&fl=*".format(structure.get("id"))).json()

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
    publis = requests.get("http://api.archives-ouvertes.fr/search/?q=(docType_s:ART AND authStructId_i:{})&sort=producedDate_tdate desc&rows=100&fl=*".format(structure.get("id"))).json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date,
               "structure": structure}
    return render(request, 'publi.html', context)
