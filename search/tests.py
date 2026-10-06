from django.test import TestCase

from accounts.models import User
from hospitals.models import Hospital
from requests_app.models import ResourceRequest
from resources.models import Resource


class SearchResourceTests(TestCase):

    def setUp(self):
        self.resource = Resource.objects.create(
            name="Oxygen",
            resource_type="OXYGEN",
        )
        self.requesting_hospital = Hospital.objects.create(
            user=User.objects.create_user(username="requesting-hospital"),
            hospital_name="Requesting Hospital",
            registration_number="REQ-001",
            address="1 Main Road",
            city="Hyderabad",
            state="Telangana",
            pincode="500001",
            phone="1234567890",
            email="requesting@example.com",
            verification_status="VERIFIED",
        )
        self.providing_hospital = Hospital.objects.create(
            user=User.objects.create_user(username="providing-hospital"),
            hospital_name="Providing Hospital",
            registration_number="PROV-001",
            address="2 Main Road",
            city="Hyderabad",
            state="Telangana",
            pincode="500002",
            phone="0987654321",
            email="providing@example.com",
            verification_status="VERIFIED",
        )

    def test_search_displays_verified_hospitals_requesting_selected_resource(self):
        ResourceRequest.objects.create(
            requesting_hospital=self.requesting_hospital,
            providing_hospital=self.providing_hospital,
            resource=self.resource,
            quantity=10,
            priority="URGENT",
        )

        response = self.client.post(
            "/search/",
            {"resource": self.resource.pk, "quantity": 1},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Requesting Hospital")
        self.assertContains(response, "Wants:")
        self.assertContains(response, "10")

    def test_search_hides_non_pending_resource_requests(self):
        ResourceRequest.objects.create(
            requesting_hospital=self.requesting_hospital,
            providing_hospital=self.providing_hospital,
            resource=self.resource,
            quantity=10,
            status="ACCEPTED",
        )

        response = self.client.post(
            "/search/",
            {"resource": self.resource.pk, "quantity": 1},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No verified hospitals are currently requesting this resource.",
        )
