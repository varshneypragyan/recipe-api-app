"""
Tests for models.
"""
from decimal import Decimal

from django.db.models.query_utils import select_related_descend
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a new user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe_successful(self):
        """Test creating recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'test@1234'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title="Sample Recipe Title",
            time_minutes=5,
            price=Decimal('5.50'),
            description="Some sample description"
        )

        self.assertEqual(str(recipe), recipe.title)