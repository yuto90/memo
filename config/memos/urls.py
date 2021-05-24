from django.urls import path
from . import views


app_name = 'memos'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:memo_id>/', views.detail, name='detail'),
]
