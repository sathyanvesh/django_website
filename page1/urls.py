from django.urls import path
from .views import CreateView,DetailView,add_product

app_name = 'page1'

urlpatterns = [
    path('',CreateView),
    path('detail/<int:pk>',DetailView,name='detail'),
    path('addprod/',add_product,name='addprod'),
]
