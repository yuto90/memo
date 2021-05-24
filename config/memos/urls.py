from django.urls import path
from . import views


app_name = 'memos'

urlpatterns = [
    path('', views.index, name='index'),
]
