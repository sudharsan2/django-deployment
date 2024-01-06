from django.urls import path
from . import views

urlpatterns =[
    path('',views.ResumeQueryAPIView.as_view(),name='api')
]