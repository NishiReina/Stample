from django.db import models
from uuid import uuid4
from django_boost.models import AbstractEmailUser

class User(AbstractEmailUser):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, verbose_name="UUID")
