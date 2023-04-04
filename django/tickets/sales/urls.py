from django.urls import path
from sales.views import IndexView,Order

app_name='sales/'


urlpatterns = [
    
    path('',IndexView.as_view(),name='index'),
    path('reserve/<int:product_id>',Order,name='order')
]