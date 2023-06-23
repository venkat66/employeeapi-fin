from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import *


class EmployeeEndpoints(APIView):
    def get(self, request):
        endpoints = [
                {
                    'method': 'POST',
                    'url': 'http://localhost:8000/api/employee/create/',
                    'description': 'Create an employee'
                },
                {
                    'method': 'PUT',
                    'url': 'http://localhost:8000/api/employee/update/',
                    'description': 'Update an employee'
                },
                {
                    'method': 'DELETE',
                    'url': 'http://localhost:8000/api/employee/delete/',
                    'description': 'Delete an employee'
                },
                {
                    'method': 'GET',
                    'url': 'http://localhost:8000/api/employee/?regid=EMP001',
                    'description': 'Get a specific employee'
                },
                {
                    'method': 'GET',
                    'url': 'http://localhost:8000/api/employee/',
                    'description': 'Get all employees'
                }
            ]
        return Response({"endpoints":endpoints})
            

class EmployeeCreateAPIView(APIView):
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            email = request.data.get('email')
            if Employee.objects.filter(email=email).exists():
                    return Response(
                        {"message": "Employee already exists", "success": False},
                        status=status.HTTP_200_OK
                    )
            print(request.data)
            if serializer.is_valid():
                
                serializer.save()
                data = Employee.objects.filter(email=email).first()
                dataSerializer = EmployeeDetailSerializer(data)
                return Response(
                    {"message": "Employee created successfully", "regid": dataSerializer.data['regid'], "success": True},
                    status=status.HTTP_200_OK
                )
            else:
                print(serializer.errors)
                return Response(
                    {"message": "Invalid body request", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)
            return Response(
                {"message": "Employee creation failed", "success": False},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EmployeeUpdateAPIView(APIView):
    def put(self, request):
        try:
            regid = request.data.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(regid=regid)
                    serializer = EmployeeUpdateSerializer(employee, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(
                            {"message": "Employee details updated successfully", "success": True},
                            status=status.HTTP_200_OK
                        )
                    else:
                        print(serializer.errors)
                        return Response(
                            {"message": "Invalid body request", "success": False},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                except Employee.DoesNotExist:
                    return Response(
                        {"message": "No employee found with this regid", "success": False},
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    {"message": "Invalid body request", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e,'eeeeee')
            return Response(
                {"message": "Employee updation failed", "success": False},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EmployeeDeleteAPIView(APIView):
    def delete(self, request):
        try:
            regid = request.data.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(regid=regid)
                    employee.delete()
                    return Response(
                        {"message": "Employee deleted successfully", "success": True},
                        status=status.HTTP_200_OK
                    )
                except Employee.DoesNotExist:
                    return Response(
                        {"message": "No employee found with this regid", "success": False},
                        status=status.HTTP_200_OK
                    )
            else:
                return Response(
                    {"message": "Invalid body request", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                {"message": "Employee deletion failed", "success": False},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class EmployeeListAPIView(APIView):
    def get(self, request):
        try:
            regid = request.GET.get('regid')
            if regid:
                try:
                    employee = Employee.objects.get(regid=regid)
                    serializer = EmployeeSerializer(employee)
                    return Response(
                        {"message": "Employee details found", "success": True, "employees": [serializer.data]},
                        status=status.HTTP_200_OK
                    )
                except Employee.DoesNotExist:
                    return Response(
                        {"message": "No employee found with this regid", "success": False, "employees": []},
                        status=status.HTTP_200_OK
                    )
            else:
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)
                return Response(
                    {"message": "Employee details found", "success": True, "employees": serializer.data},
                    status=status.HTTP_200_OK
                )
        except Exception as e:
            return Response(
                {"message": "Employee details not found", "success": False, "employees": []},
                status=status.HTTP_200_OK
            )
