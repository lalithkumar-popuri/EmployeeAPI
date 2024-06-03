from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import APIException,ParseError

# Create your views here.

class CreateEmployeView(APIView):
    serializer_class = EmployeeSerializer
    def post(self, request):
        """
        Method to create a new employee.
        Args:
            request (Request): HTTP request object containing employee data.
        Returns:
            Response: JSON response indicating success or failure of employee creation.
        """
        try:
            serializer = EmployeeSerializer(data=request.data)
            email= request.data.get('email')
            if employee.objects.filter(email=email).exists():
                return Response({"message": "Employee already exists", "success": False}, status=status.HTTP_200_OK)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Employee created successfully", "regid": serializer.data.get('regid'), "success": True}, status=status.HTTP_200_OK)
        except serializers.ValidationError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except ParseError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Employee creation failed", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListEmployeView(APIView):
    def get(self,request,regid = None):
        """
        Method to retrieve employee details.
        Args:
            request (Request): HTTP request object.
            regid (str): Optional registration ID of the employee to retrieve.
        Returns:
            Response: JSON response containing employee details.
        """
        if regid:
            try:
                queryset = employee.objects.get(regid = regid)
                serializer = EmployeeSerializer(queryset)
                return Response({ "message" : "employee details found" , "success" :True,"employees":[serializer.data]},status=status.HTTP_200_OK)
            except employee.DoesNotExist:
                return Response({ "message" : "employee details not found" , "success" :False,"employees":[] },status=status.HTTP_200_OK)
        else:  
            queryset = employee.objects.all()
            serializer = EmployeeSerializer(queryset,many = True)
            return Response({"message":"employee details fond", "success" : True , "employees": serializer.data}, status=status.HTTP_200_OK)

class UpdateEmployeView(APIView):
    serializer_class = EmployeeSerializer
    def put(self, request,regid):
        """
        Method to update an existing employee.
        Args:
            request (Request): HTTP request object containing updated employee data.
            regid (str): Registration ID of the employee to be updated.
        Returns:
            Response: JSON response indicating success or failure of employee update.
        """
        try:
            queryset = employee.objects.get(regid=regid)
            serializer = EmployeeSerializer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Employee details updated successfully", "success": True}, status=status.HTTP_200_OK)
        except employee.DoesNotExist:
            return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)
        except serializers.ValidationError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except ParseError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"message": "Invalid body request", "success": False}, status=status.HTTP_400_BAD_REQUEST)   
        except Exception as e:
            return Response({"message": "Employee updation failed", "success": False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteEmployeView(APIView):
    def delete(self, request,regid):
        """
        Method to delete an existing employee.
        Args:
            request (Request): HTTP request object.
            regid (str): Registration ID of the employee to delete.
        Returns:
            Response: JSON response indicating success or failure of employee deletion.
        """
        try:
            queryset = employee.objects.get(regid = regid)
            queryset.delete()
            return Response({"message": "Employee deleted successfully", "success": True}, status=status.HTTP_200_OK)
        except employee.DoesNotExist:
            return Response({"message": "No employee found with this regid", "success": False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Employee deletion failed", "success": False}, status=status.HTTP_400_BAD_REQUEST)
