from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return Response(data)
