from .models import Users
from rest_framework import serializers,status 
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password  
from .utils import generate_user_account_number



class UserCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=90)
    account_balance= serializers.HiddenField(default=0)
    password=serializers.CharField(allow_blank=False,write_only=True)
    account_number= serializers.HiddenField(default=000000)  

    class Meta:
        model=Users
        fields = ['id' ,'name', 'email', 'password', 'account_balance', 'account_number']

    def validate(self, attrs): 
        
        email_exists= Users.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        
        return super().validate(attrs)  

    def create(self,validated_data):
        
        new_user=Users(**validated_data)

        new_user.password=make_password(validated_data.get('password'))
        new_user.account_number=generate_user_account_number()

        new_user.save()

        return new_user