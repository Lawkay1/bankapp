import random
from .models import Users
def generate_user_account_number():
   
    while True:
        number = random.randint(100000, 999999)
        #print(number)
        account_number_exists= Users.objects.filter(account_number=number)
        
        if not account_number_exists:
                return number
                break


