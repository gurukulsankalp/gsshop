from django.db import models

from .abstract_models import AbstractUser
from .options import ROLE_CHOICES


class Role(models.Model):
    """
    to store roles available
    """
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    """
    custom user model
    """
    roles = models.ManyToManyField(Role)

