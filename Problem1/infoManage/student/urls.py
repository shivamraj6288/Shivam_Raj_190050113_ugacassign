from django.urls import path
from . import views

app_name='student'
urlpatterns=[
    path('',views.index,name='index'),
    path('<str:roll>/delete/',views.deleteData,name='delete'),
    path('<str:roll>/edit/',views.editData,name='edit'),
    path('add/',views.addData,name='add'),
    path('savedata/',views.saveData,name='save'),
    path('<str:roll>/editdata/',views.editField,name='editdata')
]
