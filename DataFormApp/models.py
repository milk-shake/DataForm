# models.py
import datetime
from datetime import datetime
from django.db import models

class Contribution(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    contributor_email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.amount} USD by {self.contributor_email}"
