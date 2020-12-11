from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .forms import Form

def contact(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            typ = form.cleaned_data['typ']
            source = requests.get(url)
            soup = BeautifulSoup(source.content, 'html5lib')
            headings = soup.findAll(typ)
            info = []
            for hth in headings:
                info.append(hth.text)
            return render(request, 'scrap/index.html', {'info': info})

    form = Form(request.POST)
    return render(request, 'scrap/index.html', {'form': form})
