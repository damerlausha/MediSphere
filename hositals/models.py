from django.db import models
from django.conf import settings


class Hospital(models.Model):

    VERIFICATION_STATUS = (
        ("PENDING", "Pending"),
        ("UNDER_REVIEW", "Under Review"),
        ("VERIFIED", "Verified"),
        ("REJECTED", "Rejected"),
        ("BLOCKED", "Blocked"),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    hospital_name = models.CharField(
        max_length=200
    )

    registration_number = models.CharField(
        max_length=100,
        unique=True
    )

    hospital_type = models.CharField(
        max_length=100,
        blank=True
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    pincode = models.CharField(
        max_length=10
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField()

    website = models.URLField(
        blank=True
    )

    authorized_person = models.CharField(
        max_length=200,
        blank=True
    )

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    verification_status = models.CharField(
        max_length=20,
        choices=VERIFICATION_STATUS,
        default="PENDING"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.hospital_name