from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    result = requests.get('https://api.covid19api.com/summary')
    global_summery = result.json()['Global']
    print(global_summery)
    return render(request, 'core/index.html', {'global_summery': global_summery})

