from django import template

register = template.Library()


@register.filter
def get_star(count):
    i = int(count)
    star = '★'
    return star * i