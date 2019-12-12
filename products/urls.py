from django.urls import path
from . import views
# period ( . ) means current folder
# root of app is /products

# mapping to functions in views.py
urlpatterns = [
    path('', views.index),
    path('new', views.new)
#     note that views.index is not being called, instead a reference is being passed to it
]