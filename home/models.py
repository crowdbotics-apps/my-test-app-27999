from django.conf import settings
from django.db import models


class Address(models.Model):
    "Generated Model"
    street = models.CharField(
        max_length=100,
    )
    city = models.CharField(
        max_length=100,
    )
    region = models.CharField(
        max_length=100,
    )
    country = models.CharField(
        max_length=100,
    )
    address_id = models.ForeignKey(
        "home.Address",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="address_address_id",
    )
