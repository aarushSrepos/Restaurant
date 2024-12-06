from django.http import HttpResponse
from django.template import loader
from .models import TableRecord, OrderRecord

def index(request):
    status = TableRecord.objects.all()
    template = loader.get_template("base.html")
    context = {
        "status" : status,
    }
    return HttpResponse(template.render(context, request))

def specificOrder(request, table):
    status = OrderRecord.objects.filter(tableNumber=table)
    template = loader.get_template("specificOrder.html")
    context = {
        "status" : status,
    }
    return HttpResponse(template.render(context, request))   