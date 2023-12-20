from decimal import Decimal
from math import modf

from django import template

from content_creator.models import Creator

register = template.Library()


@register.filter(name="stars")
def stars(value: Decimal):
    full_stars = int(value)
    half_stars = 1 if modf(value)[0] >= 0.5 else 0
    empty_stars = 5 - full_stars - half_stars

    return range(full_stars), range(half_stars), range(empty_stars)

@register.filter(name="platform_name")
def platform_name(value: str):
    platform_dict = {code: name for code, name in Creator.PLATFORM_CHOICES}
    return platform_dict[value]