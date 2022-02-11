from django.http import response
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from student_management.models import Student
from .serializers   import StudentSerializer

from api import serializers

@api_view(['GET'])
def get_details(request):
  students = Student.objects.all()
  serializer = StudentSerializer(students, many = True)
  return Response(serializer.data) 
 
@api_view(['GET'])
def get_detail(request,pk):  
    students = Student.objects.get(id=pk)
    serializer = StudentSerializer(students, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def create_detail(request): 
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def update_detail(request,pk):
    students = Student.objects.get(id=pk)   
    serializer = StudentSerializer(instance=students,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def delete_detail(request,pk): 
    students = Student.objects.get(id=pk) 
    students.delete()

    return Response('Item successfully delete!')


