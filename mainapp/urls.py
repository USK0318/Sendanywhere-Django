from django.urls import path
from . import views

urlpatterns=[
    path('',views.display0,name='main'),
    path('send/',views.display,name='sendurl'),
    path('retrive/',views.display2,name='reciveurl'),
    path('retrive/del/<int:pk>',views.delet,name='deleturl'),
]
