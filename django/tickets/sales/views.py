from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from sales.models import Products,Reserve
from sales.forms import ReserveForm
from django.urls import reverse_lazy
class IndexView(ListView):
    template_name='sales/HomePage.html'
    model=Products
   

class OrderView(CreateView):
    model=Reserve
    form_class=ReserveForm
    template_name='sales/OrderForm.html'
    success_url=reverse_lazy('sales:index')                 #Перекинуть на страницу оплаты
   
        