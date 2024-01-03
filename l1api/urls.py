from django.urls import path
from . import views

urlpatterns =[
    path('',views.func1,name='api')
]