from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from sales.models import Products,Reserve
from sales.forms import ReserveForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

class IndexView(ListView):
    template_name='sales/HomePage.html'
    model=Products
   

# class OrderView(CreateView):
#     model=Reserve
#     form_class=ReserveForm
#     template_name='sales/OrderForm.html'
#     success_url=reverse_lazy('sales:index')                 #Перекинуть на страницу оплаты


   
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
            
            return HttpResponseRedirect(reverse('sales:index'))
    else:
        form=ReserveForm()
    
    context={'form':form,'product':product_id,'quantity':place}
    return render(request,'sales/OrderForm.html',context)