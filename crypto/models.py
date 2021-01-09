from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class VC(models.Model):
    CHOICES = [
        ('XRP', 'XRP'),
        ('ETH', 'Ethereum'),
    ]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_open = models.DateTimeField()
    amount_invested = models.IntegerField()
    buy_price = models.FloatField()
    date_closed = models.DateTimeField(blank=True, null=True)
    sell_price = models.FloatField(blank=True, null=True)
    loss_profit = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    currency = models.CharField(max_length=300, choices=CHOICES)
    
    

