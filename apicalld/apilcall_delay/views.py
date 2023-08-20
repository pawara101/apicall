from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Apicall

from .serializers import ApicallSerializer
# Create your views here.

import time,random

class ApicallApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        todos = Apicall.objects.filter(user = request.user.id)
        serializer = ApicallSerializer(todos, many=True)
        
        resp_time = random.randint(1,100)
        

        # time.sleep(resp_time)
        return Response({
            'message': f'Delay with {resp_time} secconds'
        })
    