from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    result = requests.get('https://api.covid19api.com/summary')
    print(result.json())
    return render(request, 'core/index.html', {'result': result})