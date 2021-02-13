from django.shortcuts import render

# request the api and get the json back
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employess
from .serializers import employeeSerializer

class employeeList(APIView):

    def get(self,request):
        employess1=employess.objects.all()
        serializer=employeeSerializer(employess1,many=True)
        return Response(serializer.data)

    def post(self):
        pass    