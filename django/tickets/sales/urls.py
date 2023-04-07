from django.urls import path
from sales.views import Order,Sort

app_name='sales/'


urlpatterns = [
    
    path('reserve/<int:product_id>',Order,name='order'),
    path('',Sort,name='index'),
    
    
]