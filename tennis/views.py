from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TennisRacketBrands
# Create your views here.

def allRacketsView(request):
    all_racket_items = TennisRacketBrands.objects.all()
    return render(request, 'brands.html', {'all_items': all_racket_items})

def addRasketView(request):
    new_item = TennisRacketBrands(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/final/')


def resultView(request):
    last_result = TennisRacketBrands.objects.last()
    return render(request, 'pict.html', {'your_choise': last_result.content})