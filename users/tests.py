from django.test import TestCase

from .models import User


class UserTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="test", password="test")

    def test_create_user(self):
        user = User.objects.get(username="test")
        self.assertIsNotNone(user)
