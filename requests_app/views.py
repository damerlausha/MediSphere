from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ResourceRequest


@login_required
def request_list(request):

    requests = ResourceRequest.objects.none()

    if request.user.role == "HOSPITAL":

        try:

            hospital = request.user.hospital

            requests = ResourceRequest.objects.filter(

                requesting_hospital=hospital

            ) | ResourceRequest.objects.filter(

                providing_hospital=hospital
            )

        except Exception:

            requests = ResourceRequest.objects.none()

    return render(

        request,

        "requests/list.html",

        {
            "requests": requests
        }
    )