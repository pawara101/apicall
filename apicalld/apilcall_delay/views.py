from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Apicall

from .serializers import ApicallSerializer
# Create your views here.


class ApicallApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        todos = Apicall.objects.filter(user = request.user.id)
        serializer = ApicallApiView(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)