from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class betacls(APIView):
    def post(self,request):
        value = request.data.get('value')
        return Response("Hey Buddy")