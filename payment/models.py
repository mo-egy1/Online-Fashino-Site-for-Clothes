from django.db import models
from uuid import uuid4
from user.models import User

STATE = (
    ('success','success'),
    ('cancel','cancel'),
)
class Payment (models.Model) : 
    user = models.ForeignKey(User,related_name='user_payment',on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=10,choices=STATE,editable=False)
    id = models.UUIDField(default=uuid4,primary_key=True,editable=False)
