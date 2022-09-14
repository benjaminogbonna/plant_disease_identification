from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('c', views.camera, name='c'),
    path('anthracnose', views.anthracnose, name='anthracnose'),
    path('cercospora_leaf_spot', views.cls, name='cls'),
    path('phosphorus_deficiency', views.pd, name='pd'),
]
