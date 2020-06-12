from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *

# Create your views here.


def index (request):
    item_list = Item.objects.all()

    for item in item_list:
        item.item_count = item.itemmodel_set.count()
        a = item.itemmodel_set.all()

        n = 0

        for i in a:
            n = n + i.item_count
        item.total_unit = n


    context = {'item_list' : item_list,
    }
    return render(request, 'index.html', context)


def add_model(request):
    mname = request.POST["mname"]
    itemno = request.POST["itemno"]
    itemprice = request.POST["itemprice"]
    itemtype = request.POST["itemtype"]
    newitem = Item.objects.get(pk=itemtype)

    newmodel = newitem.itemmodel_set.create(model_name = mname, item_count = itemno, item_price = itemprice)
    return render(request, 'index.html')


def detail(request, item_id):
    try:
        item = Item.objects.get(pk = item_id)
        item.item_count = item.itemmodel_set.count()
    except Item.DoesNotExist :
        raise Http404("The Item Does not Exist")
    return render(request, 'detail.html', {'item' : item})
