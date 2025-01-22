from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [

    path('',views.createbook,),
    path('listview/', views.list,name='list'),
    path('view/<int:book_id>',views.viewlist,name='view'),
    path('update/<int:book_id>',views.updatebook,name='Update'),
    path('delect/<int:book_id>',views.delect,name='Delete')

]
