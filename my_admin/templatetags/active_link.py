from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, url_name):

    request = context["request"]

    if url_name in request.path:
        return 'active'
    return ""
