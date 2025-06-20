from django import template
from products.models import TagsModel


register = template.Library()

@register.simple_tag
def category_tags():

    return TagsModel.objects.all()