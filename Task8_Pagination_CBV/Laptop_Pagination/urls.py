from .views import homepage, ShowLaptops

from django.urls import path

urlpatterns=[
    path('',homepage, name='home'),
    path('showlaptop/',ShowLaptops.as_view(), name='showlaptop')
]