from django.urls import path 
from . import views 

urlpatterns = [
    path('deposit/', views.Deposit.as_view(), name='user-creation'),
    path('balance/', views.Balance.as_view(), name='user-balance'),
    path('withdraw/', views.Withdraw.as_view(), name='withdrawal'),
    path('transfer/', views.Transfer.as_view(), name= 'transfer'),

]