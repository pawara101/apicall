from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Apicall

from .serializers import ApicallSerializer
# Create your views here.

import time

class ApicallApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):

        todos = Apicall.objects.filter(user = request.user.id)
        serializer = ApicallSerializer(todos, many=True)
        resp_time = 2
        time.sleep(resp_time)
        return Response({
            'message': f'Delay with {resp_time} secconds'
        })
    
    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = ApicallSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)