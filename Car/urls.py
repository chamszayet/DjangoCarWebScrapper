
from django.urls import path
from .views import  CarAPIView,CarDetails , CarFilterList

urlpatterns = [
    
    
    path('cars/',CarAPIView.as_view()), 
    path('detail/<int:id>/',CarDetails.as_view()),
    
    
    path('',CarAPIView.as_view()), 

    path('filter/', CarFilterList.as_view())

    



]