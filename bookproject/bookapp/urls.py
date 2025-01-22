
from django.urls import path
from . import views

urlpatterns = [

    path('',views.createbook),
    path('listview/', views.list),
    path('view/<int:book_id>',views.viewlist),
    path('update/<int:book_id>',views.updatebook)

]
