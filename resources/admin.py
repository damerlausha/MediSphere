
from django.contrib import admin
from .models import Resource, Availability


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "resource_type",
        "unit",
    )

    list_filter = (
        "resource_type",
    )

    search_fields = (
        "name",
        "description",
    )


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):

    list_display = (
        "hospital",
        "resource",
        "quantity",
        "is_available",
        "source_type",
        "last_updated",
    )

    list_filter = (
        "is_available",
        "source_type",
    )

    search_fields = (
        "hospital__hospital_name",
        "resource__name",
    )