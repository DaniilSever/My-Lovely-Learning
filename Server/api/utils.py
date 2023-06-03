from unidecode import unidecode
from django.template.defaultfilters import slugify
from rest_framework.serializers import Serializer

def make_slug(string):
    return slugify(unidecode(string))

def save_serializer(serializer: Serializer):
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)