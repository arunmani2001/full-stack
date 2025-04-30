from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns = [
    path('upload/', views.upload_rtc, name='upload_rtc'),
    path('', views.list_rtc, name='list_rtc'),
    path('fetch/', views.fetch_missing_years, name='fetch_missing'),
]