from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from register.serializers import RegisterSerializer
from register.models import Register

# Create your views here.


class RegisterList(APIView):
    def get(self, request, format=None):
        queryset = Register.objects.all().order_by('id')
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
