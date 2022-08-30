from django.urls import path
from . import views


app_name = 'base'
urlpatterns = [
    path('<str:query>',views.SearchGif),
    path('',views.getData),
]
