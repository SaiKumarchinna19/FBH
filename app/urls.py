from django.urls import path
from .import views
urlpatterns=[
    path('',views.create,name='create'),
    path('1',views.profile,name='profile'),
    path('2',views.pin,name='pin'),
    path('3',views.valid_otp,name='valid_otp'),
    path('4',views.deposite,name='deposite'),
    path('5',views.bal,name='bal'),
    
    path('6',views.withdraw,name='withdraw'),
    path("7",views.transfer,name='transfer')

]

 
