from unidecode import unidecode
from django.template.defaultfilters import slugify

def make_slug(string):
    return slugify(unidecode(string))