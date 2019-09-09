from django.db import models

from core.model_utils import BaseModel
from core.models import User


class Item(BaseModel):
    description = models.TextField(max_length=1024)
    address = models.CharField(max_length=255)
    geopoint = models.CharField(max_length=100)

    waste_disposer = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='items_disposed'
    )
