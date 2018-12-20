from django.shortcuts import render


def index(request):
    import requests
    from time import strftime
    from time import gmtime

    publis = requests.get('http://api.archives-ouvertes.fr/search/3S-R?fq=docType_s:ART&sort=producedDate_tdate desc&rows=100&fl=*').json()

    date = strftime("%d/%m/%Y", gmtime())
    context = {"publis": publis["response"]["docs"],
               "publis3": publis["response"]["docs"][:3],
               "publis5": publis["response"]["docs"][:5],
               "date": date}
    return render(request, 'publi.html', context)
