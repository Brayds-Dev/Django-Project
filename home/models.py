from django.conf import settings
from django.db import models

# Create your models here.

class Item(models.Model):
    # A tuple containing a selection of choices for the items condition
    CONDITION_CHOICES = [
        ("New", "Brand new condition"),
        ("Good", "Near new condition well looked after"),
        ("OK", "Average condition"),
        ("Bad", "Poor condition old and well worn"),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    # Using djangos preffered currency data type
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=20)
    # Each item listed will need to be assigned a user
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title + '-' + self.user.first_name