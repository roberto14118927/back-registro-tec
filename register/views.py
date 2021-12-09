from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from register.serializers import RegisterSerializer
from register.serializers import TeamsSerializer
from register.models import Register
from register.models import Teams
import json
# Create your views here.


class RegisterList(APIView):
    def get(self, request, format=None):
        queryset = Register.objects.filter(status = False).order_by('id')
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamsList(APIView):
    def get(self, request, format=None):
        queryset = Teams.objects.all().order_by('id')
        serializer = TeamsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        body_unicode = request.body
        body_json = json.loads(body_unicode)
        conta = int((len(body_json)))
        if conta > 0:
            for x in range(conta):
                idR = body_json[x]['idR']
                nameTeam = body_json[x]['nameTeam']
                name = body_json[x]['name']
                lastName = body_json[x]['lastName']
                email = body_json[x]['email']
                addTeams = Teams(idR = idR, nameTeam = nameTeam, name = name, lastName = lastName, email = email)
                Register.objects.filter(id = int(idR)).update(status = True)
                addTeams.save()
            return Response("succes", status=status.HTTP_201_CREATED)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)

