from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link_exact(context, url_name):

    request = context["request"]

    if request.path == reverse(url_name):
        return 'active'
    return ""
