from django.urls import path
from .views import CreateView,DetailView

app_name = 'page1'

urlpatterns = [
    path('',CreateView),
    path('detail/<int:pk>',DetailView,name='detail'),
]
