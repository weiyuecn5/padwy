from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<zhid>/<st>/<dj>/<cw>/',views.add,name='add'),
    path('xq/<zhid>/',views.xq,name='xq'),
    path('ks/<zhid>/',views.ks,name='ks'),
    path('delshuju/<zhid>/', views.delshuju, name='delshuju')
]