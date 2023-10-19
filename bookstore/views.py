from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def allbooks(request):
    return Response('List of the books', status=status.HTTP_200_OK)

def book(request):
    return None