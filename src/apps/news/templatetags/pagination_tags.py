from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context["request"].GET.copy()
    for kwarg in kwargs:
        try:
            query.pop(kwarg)
        except KeyError:
            pass

    query.update(kwargs)
    url_path = f"{context['request'].path}?{query.urlencode()}"
    safe_url_path = mark_safe(url_path)
    return safe_url_path
