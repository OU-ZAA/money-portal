from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    balance = models.FloatField(default=10000.00)

    def serialize(self):
        return {
            "balance": self.balance
        }


class Transaction(models.Model):
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=25)
    memo = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def serialize(self): 
        return {
            "id": self.id,
            "amount": self.amount,
            "transaction_type": self.transaction_type,
            "memo": self.memo,
            "created_at": self.created_at.strftime("%b %d %Y, %I:%M %p"),
            "user": self.user.username
        }

    def __str__(self):
        return self.memo

