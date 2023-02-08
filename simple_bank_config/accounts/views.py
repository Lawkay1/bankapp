from django.shortcuts import render

# Create your views here.


from rest_framework import generics, status
from rest_framework.response import Response 
from .models import Users
from . import serializers




class UserCreationView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            data = serializer.data
            user = Users.objects.get(pk=data['id'])
            user_account_number = user.account_number
            data['account_number'] = user_account_number             
            

                  
            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.




