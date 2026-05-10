import pytest
from rest.client import ClubClient


@pytest.fixture
def client():
    return ClubClient()