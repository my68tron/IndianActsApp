from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    '''To use most of the features of BaseUserManager and override a couple of methods'''

    def create_user(self, email, password=None, **extra_fields):
        '''Create and save a new user'''

        # Raise ValueError if email is not present or None
        if not email:
            raise ValueError('Users must have an email ID!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        '''Creates a new superuser'''

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that supports email instead of username'''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # Which field should be used as username for login
    USERNAME_FIELD = 'email'

    class Meta:
        # To give custom name to the table in database
        db_table = 'users'
