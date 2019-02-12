from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def index(request):
    # return render(request, 'web3sr.html')
    return HttpResponseRedirect(reverse('publi:index'))
