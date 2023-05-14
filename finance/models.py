from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    balance = models.FloatField(default=10000.00)


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
            "created_at": self.created_at
        }

    def __str__(self):
        return self.memo

