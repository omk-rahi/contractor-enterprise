from django import template

register = template.Library()

@register.simple_tag
def status_class(status):
    if status.lower() in ['delivered', 'completed', 'available']:
        return 'success'
    
    elif status.lower() in ['canceled', 'failed', 'rejected', 'sold']:
        return 'danger'
    
    elif status.lower() in ['in_process', 'pending']:
        return 'warning'
    
    elif status.lower() in ['confirmed']:
        return 'info'

    else:
        return 'dark'