

from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Emp
from rest_framework import status
from django.shortcuts import render

class UserView(APIView):
    def get(self, request):
            model = Emp.objects.all()
            serializer = EmpSerializer(model, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
            serializer = EmpSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )