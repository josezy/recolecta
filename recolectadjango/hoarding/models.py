import re

from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

from optimized_image.fields import OptimizedImageField
from multiselectfield import MultiSelectField

from core.model_utils import BaseModel
from core.models import User
from core.constants import PICKUP_TIMES
from core.utils import image_path


class Item(BaseModel):
    waste_disposer = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='items_disposed'
    )
    description = models.TextField(max_length=1024)
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    geopoint = models.CharField(max_length=100)

    pickup_times = MultiSelectField(choices=PICKUP_TIMES)

    @cached_property
    def coords(self):
        lon, lat = re.search('\((.+?)\)', self.geopoint).group(1).split()
        return lat, lon

    @cached_property
    def latitude(self):
        return self.coords[0]

    @cached_property
    def longitude(self):
        return self.coords[1]

    @cached_property
    def default_image(self):
        if hasattr(self, 'photos'):
            try:
                url = self.photos.primary_photo.url
            except ValueError:
                pass
            else:
                return url
        return f'{settings.STATIC_URL}{settings.DEFAUL_RENT_IMAGE}'

    @cached_property
    def images(self):
        if hasattr(self, 'photos'):
            images = [
                listing_image.photo.url
                for listing_image in self.photos.listingphoto_set.all()
                if listing_image.photo
            ]
            images.insert(0, self.default_image)
            return images
        return [self.default_image]


class ItemPhotos(BaseModel):
    listing = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        related_name='photos'
    )
    primary_photo = OptimizedImageField(
        upload_to=image_path,
        null=True,
        blank=True
    )


class ItemPhoto(BaseModel):
    listing = models.ForeignKey(ItemPhotos, on_delete=models.CASCADE)
    photo = OptimizedImageField(
        upload_to=image_path,
        blank=True
    )
