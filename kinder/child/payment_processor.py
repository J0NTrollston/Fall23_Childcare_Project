from django.db import models
from .models import enrollments
from .models import payment

classroom = enrollments.Classroom
price = payment.price
transactionID = payment.transactionID
startDate = enrollments.startDate

def Price(classroom):
    if classroom == 'Infant':
        price = 300

    elif classroom == 'Toddler':
        price = 275

    elif classroom == 'Twadler' :
        price = 250

    elif classroom == '3 Years Old':
        price = 225

    elif classroom == '4 Years Old':
        price = 200

    else:
        print('Not a valid classroom')

    return price


#def Payment(transaction_ID, price):
    #if(startDate)