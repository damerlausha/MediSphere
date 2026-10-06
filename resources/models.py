from django.db import models
from hospitals.models import Hospital


class Resource(models.Model):

    RESOURCE_TYPE_CHOICES = (
        ("BLOOD", "Blood & Blood Components"),
        ("MEDICINE", "Medicines"),
        ("OXYGEN", "Oxygen & Respiratory"),
        ("SPECIALIST", "Specialist / Doctor"),
        ("EMERGENCY", "Emergency Services"),
        ("OTHER", "Other"),
    )

    name = models.CharField(max_length=200)

    resource_type = models.CharField(
        max_length=30,
        choices=RESOURCE_TYPE_CHOICES
    )

    description = models.TextField(blank=True)

    unit = models.CharField(
        max_length=50,
        default="units"
    )

    def __str__(self):
        return self.name


class Availability(models.Model):

    SOURCE_CHOICES = (
        ("MANUAL", "Manual"),
        ("API", "API"),
        ("SYSTEM", "System"),
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="availabilities"
    )

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="availabilities"
    )

    quantity = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
        default="MANUAL"
    )

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hospital.hospital_name} - {self.resource.name}"