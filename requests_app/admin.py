from django.contrib import admin

from .models import ResourceRequest


@admin.register(ResourceRequest)
class ResourceRequestAdmin(admin.ModelAdmin):

    list_display = (

        "requesting_hospital",

        "providing_hospital",

        "resource",

        "quantity",

        "priority",

        "status",

        "created_at",
    )

    list_filter = (

        "priority",

        "status",
    )