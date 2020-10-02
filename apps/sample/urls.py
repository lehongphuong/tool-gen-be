from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    # *******************************************************
    # begin Customer
    path('gencode', views.gencode, name='gencode'),
    path('createDataCustomer', views.createDataCustomer, name='createDataCustomer'),
    path('readDataCustomer', views.readDataCustomer, name='readDataCustomer'),
    path('updateDataCustomer', views.updateDataCustomer, name='updateDataCustomer'),
    path('deleteDataCustomer', views.deleteDataCustomer, name='deleteDataCustomer'),
    path('findDataCustomer', views.findDataCustomer, name='findDataCustomer'),
    path('find_custommer_by_status', views.find_custommer_by_status, name='find_custommer_by_status'),
    path('find_custommer_between_date', views.find_custommer_between_date, name='find_custommer_between_date'),
    # end Customer
    # *******************************************************
]
