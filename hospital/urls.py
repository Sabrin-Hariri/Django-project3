from django.contrib import admin
from django.urls import path
from .views import *


##############################

app_name = 'hospital'


urlpatterns = [
    path('', HomePage.as_view() , name = 'home'),
    path('thanks/', Thanks.as_view() , name = 'thanks'),
    path('create/', Create.as_view() , name = 'create'),
    path('show/', Show.as_view() , name = 'show'),
    path('details/<int:pk>', Detail.as_view() , name = 'details'),
    path('update/<int:pk>', Update.as_view() , name = 'update'),
    path('delete/<int:pk>', Delete.as_view() , name = 'delete'),

]
