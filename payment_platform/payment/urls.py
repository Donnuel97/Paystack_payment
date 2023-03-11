from django.urls import path
from . import views

urlpatterns = [
    #leave as empty string for base url
    path('', views.initiate_payment, name="initiate_payment"),
    path('<str:ref>/', views.verify_payment, name='verify-payment')
    
]