from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns = [
    path('',views.Home,name="Home"), 
    path('addData',views.AddData,name="addData")
]