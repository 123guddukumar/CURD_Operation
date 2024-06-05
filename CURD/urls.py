from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('add/',add,name='add'),
    path('edit/',edit,name='edit'),
    path('update/<str:id>',update,name='update'),
    path('delete/<str:id>',delete,name='delete'),
]
