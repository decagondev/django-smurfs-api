from django.db import models
from uuid import uuid4

# Create your models here.

class Smurf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=300)
    age = models.CharField(max_length=200)
    height = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
