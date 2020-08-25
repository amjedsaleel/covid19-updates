from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    result = requests.get('https://api.covid19api.com/summary')
    json = result.json()
    global_summery = json['Global']
    countries = json['Countries']
    return render(request, 'core/index.html', {'global_summery': global_summery, 'countries': countries})

