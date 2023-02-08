from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response 
from accounts.models import Users
from . import serializers
from rest_framework.permissions import IsAuthenticated

# Create your views here.
User = get_user_model()
class Deposit(generics.GenericAPIView):
    serializer_class = serializers.DepositSerializers
    permission_classes=[IsAuthenticated]

    def post(self, request):
        data = request.data
        print(data)
        user = request.user 
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        deposit_amount = serializer.validated_data['deposit_amount']
        print(deposit_amount)
        user.account_balance += deposit_amount
        user.save()

        data = {
            'new balance': user.account_balance
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

class Balance(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]

    def get(self, request): 
        user = request.user 
        #user_instance = Users.objects.get(pk=user.id)

        data = {
            'balance': user.account_balance
        }

        return Response(data=data ,status=status.HTTP_200_OK)

class Withdraw(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]

    serializer_class= serializers.WithdrawalSerializers
    def post(self, request):
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            user = request.user
            
            user_balance = user.account_balance
            withdrawal_amount= serializer.validated_data['withdrawal_amount']

            if user_balance >= withdrawal_amount:
                user.account_balance = user.account_balance - withdrawal_amount  
                user.save()

                data = { 
                    'message': 'success',
                    'balance': user.account_balance
                }

                return Response(data = data, status = status.HTTP_202_ACCEPTED)
            
            data = {
                'error': 'you have insufficient balance to make this withdrawal'
                        }

            return Response(data=data , status= status.HTTP_403_FORBIDDEN)

class Transfer(generics.GenericAPIView): 
    permission_classes=[IsAuthenticated]
    serializer_class= serializers.TransferSerializers

    def post(self,request):
        data= request.data
        user = request.user 
        serializer= self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        destination_account = serializer.validated_data['destination_account']
        transfer_amount= serializer.validated_data['transfer_amount']

        destination_user = Users.objects.filter(account_number=destination_account).first()

        if destination_user:
            
            if user.account_balance >= transfer_amount:
                user.account_balance = user.account_balance - transfer_amount
                destination_user.account_balance = destination_user.account_balance 
                user.save()
                destination_user.save()
                data = {
                'message': 'transfer succesful',
                'balance': user.account_balance
            }

                return Response(data=data, status=status.HTTP_202_ACCEPTED)

            
            else:
                data = {
                    'message': 'insufficient balance'
                    
                }
                return Response(data=data, status=status.HTTP_403_FORBIDDEN)

        data = {
            'message': 'Invalid account'
            
        }
        return Response(data=data, status= status.HTTP_404_NOT_FOUND)




