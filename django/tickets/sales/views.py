from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from sales.models import Products,Reserve
from sales.forms import ReserveForm,Sotrform
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
import datetime
from pycbrf.toolbox import ExchangeRates
from django.utils import timezone



class IndexView(ListView):
    template_name='sales/HomePage.html'
    model=Products
   





   
def Order(request,product_id):
    product=Products.objects.get(id=product_id)
    place=product.quantity

    if request.method=='POST':
        form=ReserveForm(data=request.POST)
        
        if form.is_valid():
            
            quan=form.cleaned_data.get("reserve_quantity")
            product.quantity-=quan
            product.save()
            form.instance.booking=product
            form.save()
            rates = ExchangeRates(str(datetime.datetime.now().date()))
            result = rates['EUR']
            
            summa=quan*product.price
            summa_eur=round(summa/(round(result.value,2)))
            context={'product':product,'quantity':quan,'sum':summa,'eur_sum':summa_eur}
            return render(request,'sales/Payment.html',context=context)
    else:
        form=ReserveForm()

    
    context={'form':form,'product':product_id,'quantity':place}
    return render(request,'sales/OrderForm.html',context)
def Sort(request):

    if request.method=='POST':
        form=Sotrform(data=request.POST)
        if form.is_valid():
            product_start=form.cleaned_data.get('start_punkt')
            product_finish=form.cleaned_data.get('finish_punkt')
            product_date=form.cleaned_data.get('date')
            product=Products.objects.filter(start_punkt=product_start,finish_punkt=product_finish,date=product_date)
            context={'form':form,'products':product}
            
    else:
        form =Sotrform()
        product=Products.objects.filter(date=datetime.datetime.now().date())
        context={'form':form,'products':product}
    return render(request,'sales/HomePage.html',context)

def SeeCancel(request):
    return render(request,'sales/CancelOrder.html')


def AutoDelete(request):
    reserve=Reserve.objects.all()
    for object in reserve:
        if (object.is_paid==False) and (((timezone.now() - object.date_create).total_seconds() > 30)):
            object.delete()
    return render(request,'sales/HomePage.html')