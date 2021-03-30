from django.urls import path

from . import views

app_name='basic_matcher'
urlpatterns = [
     path('', views.index, name = 'index'),
     path('results/', views.find_candidate, name = 'results'),
]