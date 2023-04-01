from django.urls import path
from sales.views import IndexView,OrderView

app_name='sales/'


urlpatterns = [
    
    path('',IndexView.as_view(),name='index'),
    path('reserve/',OrderView.as_view(),name='order')
]