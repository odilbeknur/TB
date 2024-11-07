from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})


@register.filter(name='add')
def add(value, arg):
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return value  
