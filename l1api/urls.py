from django.urls import path
from . import views

urlpatterns =[
    path('<str:pk>',views.ResumeQueryAPIView.as_view(),name='api')
]