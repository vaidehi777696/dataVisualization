from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun,name='datafun')
]