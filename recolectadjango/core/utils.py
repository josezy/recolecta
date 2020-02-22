import os
import re
import uuid
import random

from enum import Enum

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import (
    DecimalField, CharField, IntegerField, AutoField, QuerySet
)


class StrBasedEnum(Enum):
    @classmethod
    def from_str(cls, string: str):
        return cls._member_map_[string.upper()]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ExtendedEncoder(DjangoJSONEncoder):
    """
    Extended json serializer that supports serializing several model
    fields and objects
    """

    def default(self, obj):
        cls_name = obj.__class__.__name__

        if isinstance(obj, (DecimalField, CharField)):
            return str(obj)

        elif isinstance(obj, (IntegerField, AutoField)):
            return int(obj)

        elif cls_name in ('Action', 'Event'):
            return obj.name

        elif hasattr(obj, '__json__'):
            return obj.__json__()

        elif isinstance(obj, QuerySet):
            return list(obj)

        elif isinstance(obj, uuid.UUID):
            return str(obj)

        elif isinstance(obj, bytes):
            return obj.decode()

        elif cls_name == 'CallableBool':
            # ^ shouldn't check using isinstance because CallableBools
            #   will eventually be deprecated
            return bool(obj)

        elif cls_name == 'AnonymousUser':
            # ^ cant check using isinstance since models aren't ready
            #   yet when this is called
            return None  # AnonUser should always be represented as null in JS

        elif isinstance(obj, StrBasedEnum):
            return str(obj)

        elif cls_name in ('dict_items', 'dict_keys', 'dict_values'):
            return tuple(obj)

        return DjangoJSONEncoder.default(self, obj)

    @classmethod
    def convert_for_json(cls, obj, recursive=True):
        if recursive:
            if isinstance(obj, dict):
                return {
                    cls.convert_for_json(k): cls.convert_for_json(v)
                    for k, v in obj.items()
                }
            elif isinstance(obj, (list, tuple)):
                return [cls.convert_for_json(i) for i in obj]

        try:
            return cls.convert_for_json(cls().default(obj))
        except TypeError:
            return obj


def convert_to_snake(name):
    """
    Converts camelCase string to snake_case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def image_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return '/'.join([
        str(instance.id),
        f"{randomstr}{file_extension}"
    ])


def avatar_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return '/'.join([
        str(instance.id),
        f"avatar{file_extension}"
    ])


def validate_file_size(value):
    try:
        if value.size > settings.MAX_FILE_SIZE:
            max_size = settings.MAX_FILE_SIZE // 10**6
            raise ValidationError(
                f"The maximum file size that can be uploaded is {max_size}MB")
    except FileNotFoundError:
        pass

    return value


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
