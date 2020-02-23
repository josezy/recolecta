
from django.db import models
from django.contrib.auth.models import AbstractUser

from core.model_utils import BaseModel
from core.constants import USER_TYPES
from core.utils import avatar_path, validate_file_size


class User(AbstractUser, BaseModel):
    # id = models.UUIDField
    # password
    # email
    # first_name
    # last_name
    # is_active
    # is_staff
    # is_superuser
    # last_login
    # date_joined

    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to=avatar_path,
        validators=[validate_file_size],
        blank=True, null=True
    )
    user_type = models.CharField(max_length=255, choices=USER_TYPES)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.get_full_name()

    def __json__(self, *attrs):
        return {
            **self.attrs(
                'id',
                'email',
                'first_name',
                'last_name',
                'phone',
                'bio',
                'date_joined',
                'is_active',
                'is_staff',
                'is_superuser',
                'is_authenticated',
                'user_type',
            ),
            'str': str(self),
            **(self.attrs(*attrs) if attrs else {}),
        }
