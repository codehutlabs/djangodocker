from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from mixer.backend.django import mixer
from website.views import home

import pytest


@pytest.mark.django_db
class TestViews:
    def test_home(self):
        path = reverse('home')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)
        response = home(request)

        assert response.status_code == 200, "status_code should equal 200"
