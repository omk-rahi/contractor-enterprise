from django import template

register = template.Library()

@register.simple_tag
def status_class(status):
    if status in ['delivered', 'completed']:
        return 'success'
    
    elif status in ['canceled', 'failed', 'rejected']:
        return 'danger'
    
    elif status in ['in_process', 'pending']:
        return 'warning'
    
    elif status in ['confirmed']:
        return 'info'

    else:
        return 'dark'