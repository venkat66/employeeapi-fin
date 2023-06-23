from django.urls import path
from .views import *

urlpatterns = [
    path('',EmployeeEndpoints.as_view(),name='employee-endpoints'),
    path('employee/create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('employee/update/', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('employee/delete/', EmployeeDeleteAPIView.as_view(), name='employee-delete'),
    path('employee/', EmployeeListAPIView.as_view(), name='employee-list'),
]
