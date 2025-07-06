from django.urls import path
from . import views as vs

app_name = 'store'

urlpatterns = [
    path('',vs.index,name='index'),
    path('catalog/',vs.catalog,name='catalog')
]