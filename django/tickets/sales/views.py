from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from sales.models import Products
class IndexView(ListView):
    template_name='sales/HomePage.html'
    model=Products


class OrderView(TemplateView):
    template_name='sales/OrderForm.html'