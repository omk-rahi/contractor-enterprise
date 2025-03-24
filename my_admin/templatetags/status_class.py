from django import template

register = template.Library()

@register.simple_tag
def status_class(status):
    if status.lower() in ['delivered', 'completed', 'available', 'Approved']:
        return 'success'
    
    elif status.lower() in ['canceled', 'failed', 'rejected', 'sold']:
        return 'danger'
    
    elif status.lower() in ['processing', 'pending']:
        return 'warning'
    
    elif status.lower() in ['shipped', 'out for delivery']:
        return 'info'

    else:
        return 'dark'