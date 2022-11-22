import pytest
from django.urls import resolve, reverse


def test_all_profiles():
    assert reverse("all-profiles") == "/api/v1/profiles/all/" # all-profiles is the name of the url path