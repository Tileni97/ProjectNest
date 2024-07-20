import uuid


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


# Create your models here.

class CustomUserManager(UserManager): # CustomUserManager class inherits from UserManager
    def _create_user(self,name, email, password, **extra_fields): # _create_user method takes in email, password, and extra_fields 
        if not email: # If email is not provided
            raise ValueError('The Email field must be set') # Raise a ValueError
        email = self.normalize_email(email) # Normalize the email
        user = self.model(email=email,name=name, **extra_fields) # Create a user with the email and extra_fields
        user.set_password(password) # Set the password for the user
        user.save(using=self._db) # Save the user
        return user # Return the user


    def create_user(self, name, email=None, password=None, **extra_fields): # create_user method takes in email, password, and extra_fields 
        extra_fields.setdefault('is_staff', False) # Set is_staff to False
        extra_fields.setdefault('is_superuser', False) # Set is_superuser to False
        return self._create_user(name, email, password, **extra_fields)


    def create_superuser(self, name, email, password=None, **extra_fields): # create_superuser method takes in email, password, and extra_fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')    
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin): # User class inherits from AbstractBaseUser and PermissionsMixin
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # id field is a UUIDField
    email = models.EmailField(unique=True) # email field is an EmailField
    name = models.CharField(max_length=255) # name field is a CharField
    
    is_active = models.BooleanField(default=True) # is_active field is a BooleanField
    is_staff = models.BooleanField(default=False) # is_staff field is a BooleanField
    is_superuser = models.BooleanField(default=False) # is_superuser field is a BooleanField
    
    date_joined = models.DateTimeField(auto_now_add=True) # date_joined field is a DateTimeField
    last_login = models.DateTimeField(blank=True, null=True) # last_login field is a DateTimeField

    created_at = models.DateTimeField(auto_now_add=True) # created_at field is a DateTimeField
    updated_at = models.DateTimeField(auto_now=True) # updated_at field is a DateTimeField

    objects = CustomUserManager() # objects field is an instance of CustomUserManager

    USERNAME_FIELD = 'email' # USERNAME_FIELD is set to email
    EMAIL_FIELD = 'email' # EMAIL_FIELD is set to email
    REQUIRED_FIELDS = ['name'] # REQUIRED_FIELDS is set to name

    





'''
First, we import necessary modules, including uuid for generating unique user IDs, and AbstractBaseUser, PermissionsMixin, and UserManager from django.contrib.auth.models for creating custom user management logic. The models module from Django is also imported for defining the database models.

The CustomUserManager class inherits from UserManager and contains methods to handle user creation. The _create_user method is a helper method that normalizes the email, sets the user's password, and saves the user object. The create_user method sets default values for is_staff and is_superuser to False, ensuring that regular users do not have staff or superuser privileges. The create_superuser method sets these fields to True and includes checks to ensure they are set correctly, raising a ValueError if they are not. These methods ensure that users and superusers are created with the correct attributes and security measures.

The User class inherits from AbstractBaseUser and PermissionsMixin, which provide core user authentication functionality and permissions support, respectively. The User model defines several fields: id is a UUID field to uniquely identify each user, email is an email field for user login, name is a character field for the user's name, is_active indicates if the user's account is active, is_staff indicates if the user has staff privileges, and created_at and updated_at are datetime fields to track when the user was created and last updated. The objects field uses the custom user manager CustomUserManager to handle user creation and management.

In this custom user model, USERNAME_FIELD is set to 'email', meaning email will be used as the unique identifier for authentication instead of the default username. REQUIRED_FIELDS is set to ['name'], specifying that the name field is required when creating a user.

Overall, this custom user model provides a more flexible and secure way to manage users in a Django application, allowing for email-based authentication and additional user attributes. This approach ensures that the application can handle more complex user management requirements and improves security by avoiding the use of easily guessable usernames.
'''