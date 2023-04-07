from django.urls import path
from sales.views import Order,Sort,SeeCancel

app_name='sales/'


urlpatterns = [
    
    path('reserve/<int:product_id>',Order,name='order'),
    path('',Sort,name='index'),
    path('cancel/',SeeCancel,name='cancel')
    
]