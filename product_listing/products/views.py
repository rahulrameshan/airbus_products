from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


# Create your views here.
class Productslisting(GenericAPIView):

    def get(self, request):
        return Response({"message": "success"})