from django.conf.urls import url
from django.urls import path
from .views import *
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:item_id>/', views.detail, name = 'detail'),
    path('add_model/', views.add_model, name = 'add_model'),



]
