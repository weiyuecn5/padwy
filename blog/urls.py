from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<zhid>/<st>/<dj>/<cw>/',views.add,name='add'),
    path('addid/<zhid>/<yxid>/',views.addid,name='addid'),
    path('xq/<zhid>/',views.xq,name='xq'),
    path('ks/<zhid>/',views.ks,name='ks'),
    path('wy/',views.wy,name='wy'),
    path('ww/',views.ww,name='ww'),
    path('jl/',views.jl,name='jl'),
    path('delshuju/<zhid>/', views.delshuju, name='delshuju')
]