from django.db import models
import string
import random


def create_unique_code():
    length = 6
    while True:
        char=''.join(random.choices(string.ascii_uppercase,k=length))
        if(Room.objects.filter(code=char).count() == 0):
            break
    return char




# Create your models here.
class Room (models.Model):
    code = models.CharField(max_length=10,default=create_unique_code,unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)