from django.db import models

from hospitals.models import Hospital
from resources.models import Resource


class ResourceRequest(models.Model):

    STATUS_CHOICES = (

        ("PENDING", "Pending"),

        ("ACCEPTED", "Accepted"),

        ("REJECTED", "Rejected"),

        ("COMPLETED", "Completed"),
    )

    PRIORITY_CHOICES = (

        ("NORMAL", "Normal"),

        ("URGENT", "Urgent"),

        ("EMERGENCY", "Emergency"),
    )

    requesting_hospital = models.ForeignKey(

        Hospital,

        on_delete=models.CASCADE,

        related_name="sent_requests"
    )

    providing_hospital = models.ForeignKey(

        Hospital,

        on_delete=models.CASCADE,

        related_name="received_requests"
    )

    resource = models.ForeignKey(

        Resource,

        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES,

        default="NORMAL"
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default="PENDING"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return f"Request #{self.id}"