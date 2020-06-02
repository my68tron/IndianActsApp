from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        '''Test creating  a new user with email'''

        email = 'john@example.com'
        password = 'password of john'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test that the email of new user is normalized'''

        email = 'john@ExamPle.COM'
        password = 'password of john'
        user = get_user_model().objects.create_user(email=email, password='pass1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test that creating a user with no email raises ValueError'''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='pass1234')

    def test_create_new_superuser(self):
        '''Test creating a new SuperUser'''

        user = get_user_model().objects.create_superuser(
            'john@example.com',
            'pass1234'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
