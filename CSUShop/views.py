from django.shortcuts import render
from .models import PreOrders, ListofOrders

def home(request):
    return render(request, 'index.html')

def store(request):
    return render(request, 'store.html')

def about(request):
    return render(request, 'about.html')

def preorder(request):

    pres = ListofOrders.objects.all()

    if request.method=="POST":
        name = request.POST['name']
        idnum = request.POST['idnum']
        department = request.POST['department']
        progyear = request.POST['progyear']
        contact = request.POST['contact']
        lanyardorders=PreOrders(name=name, idnum=idnum, department=department, progyear=progyear, contact=contact)
        lanyardorders.save()

    return render(request, 'preorder.html', {'pres' : pres})

