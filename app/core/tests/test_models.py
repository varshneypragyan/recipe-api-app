"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_emails_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))