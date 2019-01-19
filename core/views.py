from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import EmployeeSerializer


class StandardResultsSetPagination(PageNumberPagination):
    #for Pagination
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class ListEmployeeView(generics.ListAPIView):
    """
        Retrive all
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultsSetPagination

class CreateEmployeeView(generics.CreateAPIView):
    """
        To Create
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RetriveOneEmployeeView(generics.RetrieveAPIView):
    '''
        To Retrive One
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeleteOneEmployeeView(generics.DestroyAPIView):
    '''
        To Delete One
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateOneEmployeeView(generics.UpdateAPIView):
    '''
        To Update One
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AllOperationsEmployeeView(generics.RetrieveUpdateDestroyAPIView):
    '''
        All Operations
    '''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer