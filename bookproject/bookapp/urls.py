
from django.urls import path
from . import views

urlpatterns = [

    path('',views.createbook),
    path('listview/', views.list),

]
