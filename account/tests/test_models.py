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
