from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<zhid>/<st>/<dj>/<cw>/',views.add,name='add'),
    path('dzadd/<zhid>/<st>/<cw>/',views.dzadd,name='dzadd'),
    path('addid/<zhid>/<yxid>/',views.addid,name='addid'),
    path('sc/<zhid>/<scid>/',views.sc,name='cs'),
    path('xq/<zhid>/',views.xq,name='xq'),
    path('ks/<zhid>/',views.ks,name='ks'),
    path('wy/',views.wy,name='wy'),
    path('ww/',views.ww,name='ww'),
    path('jl/',views.jl,name='jl'),
    path('ptj/<bh1>/<bh2>/',views.ptj,name='ptj'),
    path('zhqd/',views.zhqd,name='zhqd'),
    path('delshuju/<zhid>/', views.delshuju, name='delshuju'),
    path('addsx/<zhid>/<sx>/',views.addsx,name='addsx'),
    path('addjk/<zhid>/<sx>/', views.addjk, name='addjk'),
    path('jk/', views.jk, name='jk'),
]