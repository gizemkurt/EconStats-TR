from django.http import HttpResponse
from django.shortcuts import render
from econstats.models import PriceIndex, InterestRate
from django.shortcuts import redirect




def redirect_stats(request):
    return redirect('stats/')

def interest_rate(request):
    data = InterestRate.objects.order_by('pk')
    terms = []
    values = []
    for item in data:
        term = item.term
        terms.append(term)
        value = float(item.interest_rate)
        values.append(float(value))

    context = {
        'title': 'Interest Rates for Turkey',
        'data': data,
        'labels': terms,
        'values': values
    }

    return render(request, 'econstats/interest_rate.html', context=context)


def price_indice(request):
    data = PriceIndex.objects.order_by('pk')
    terms = []
    values = []
    for item in data:
        term = item.term
        terms.append(term)
        value = float(item.price_index_rate)
        values.append(value)

    context = {
        'title': 'Price Index for Turkey',
        'data': data,
        'labels': terms,
        'values': values
    }

    return render(request, 'econstats/price_index.html', context=context)


def all_stats(request):
    data1 = InterestRate.objects.order_by('pk')
    terms1 = []
    values1 = []
    for item in data1:
        term = item.term
        terms1.append(term)
        value = float(item.interest_rate)
        values1.append(float(value))

    context = {
    }


    data2 = PriceIndex.objects.order_by('pk')
    terms2 = []
    values2 = []
    for item in data2:
        term = item.term
        terms2.append(term)
        value = float(item.price_index_rate)
        values2.append(value)

    context = {
        'title': 'Combined Statistics for Turkey',
        'title1': 'Interest Rates for Turkey',
        'title2': 'Price Index for Turkey',
        'data1': data1,
        'labels1': terms1,
        'values1': values1,
        'data2': data2,
        'labels2': terms2,
        'values2': values2
    }


    return render(request, 'econstats/all.html',  context=context)



def home(request):
    context = {

    }
    return render(request, 'econstats/home.html', context=context)
