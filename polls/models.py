from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management import defaultdict
class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
# Create your models here.