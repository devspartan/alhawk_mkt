from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_num, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError("Name Cannot Be left Blank")
        if not phone_num:
            raise ValueError("Phone number Cannot Be left Blank")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_num=phone_num,
            password=password,
        )
        print("password = " + password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, name, phone_num, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=email,
            name=name,
            phone_num=phone_num,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_num, password):

        user = self.create_user(
            email=email,
            name=name,
            phone_num=phone_num,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def is_email_registered(self, email):
        user = self.filter(email=email)
        if user.count() > 0:
            return True
        return False


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=40, null=False, blank=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    phone_num = PhoneNumberField(default='')
    add = models.CharField(max_length=1000, null=True, blank=True)
    # notice the absence of a "Password field", that's built in.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_num']  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


