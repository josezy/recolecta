from django.db import models

from core.model_utils import BaseModel
from core.models import User
from core.constants import WORKING_TIMES


class CollectionSchedule(BaseModel):
    monday = models.CharField(max_length=32, choices=WORKING_TIMES)
    tuesday = models.CharField(max_length=32, choices=WORKING_TIMES)
    wednesday = models.CharField(max_length=32, choices=WORKING_TIMES)
    thursday = models.CharField(max_length=32, choices=WORKING_TIMES)
    friday = models.CharField(max_length=32, choices=WORKING_TIMES)
    saturday = models.CharField(max_length=32, choices=WORKING_TIMES)
    sunday = models.CharField(max_length=32, choices=WORKING_TIMES)


class Item(BaseModel):
    waste_disposer = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='items_disposed'
    )
    description = models.TextField(max_length=1024)
    address = models.CharField(max_length=255)
    geopoint = models.CharField(max_length=100)

    collection_schedule = models.ForeignKey(
        CollectionSchedule,
        on_delete=models.CASCADE,
        related_name='schedule'
    )
