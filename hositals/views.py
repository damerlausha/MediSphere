from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Hospital


@login_required
def hospital_register(request):

    if request.method == "POST":

        registration_number = request.POST.get(
            "registration_number"
        )

        if Hospital.objects.filter(
            registration_number=registration_number
        ).exists():

            messages.error(
                request,
                "Hospital registration number already exists."
            )

            return redirect("hospital_register")

        hospital = Hospital.objects.create(

            user=request.user,

            hospital_name=request.POST.get(
                "hospital_name"
            ),

            registration_number=registration_number,

            hospital_type=request.POST.get(
                "hospital_type"
            ),

            address=request.POST.get(
                "address"
            ),

            city=request.POST.get(
                "city"
            ),

            state=request.POST.get(
                "state"
            ),

            pincode=request.POST.get(
                "pincode"
            ),

            phone=request.POST.get(
                "phone"
            ),

            email=request.POST.get(
                "email"
            ),

            website=request.POST.get(
                "website"
            ),

            authorized_person=request.POST.get(
                "authorized_person"
            ),

            latitude=request.POST.get(
                "latitude"
            ) or None,

            longitude=request.POST.get(
                "longitude"
            ) or None,

            verification_status="PENDING"
        )

        request.user.role = "HOSPITAL"
        request.user.save()

        messages.success(
            request,
            "Hospital registration submitted for verification."
        )

        return redirect("hospital_dashboard")

    return render(
        request,
        "hospitals/register.html"
    )


@login_required
def hospital_dashboard(request):

    try:
        hospital = Hospital.objects.get(
            user=request.user
        )
    except Hospital.DoesNotExist:

        return redirect("hospital_register")

    if hospital.verification_status != "VERIFIED":

        return render(
            request,
            "hospitals/verification.html",
            {
                "hospital": hospital
            }
        )

    return render(
        request,
        "hospitals/dashboard.html",
        {
            "hospital": hospital
        }
    )