from django.urls import path
from .views import *

urlpatterns = [
    path('', ListEmployeeView.as_view(), name="list"),
    path('create/', CreateEmployeeView.as_view(), name="create"),
    path('one/<int:pk>/', RetriveOneEmployeeView.as_view(), name="one"),
    path('delete/<int:pk>/', DeleteOneEmployeeView.as_view(), name="delete"),
    path('update/<int:pk>/', UpdateOneEmployeeView.as_view(), name="update"),
    path('alloperations/<int:pk>/', AllOperationsEmployeeView.as_view(), name="alloperations"),
]