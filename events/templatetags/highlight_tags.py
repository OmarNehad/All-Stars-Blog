from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import re
from django import template
register = template.Library()

@register.filter()
@stringfilter
def highlight(value, search):
    pattern = re.compile('(%s)' % search, re.IGNORECASE)
    highlighted = pattern.sub(r'<span class="highlight">\1</span>',value)
    return mark_safe(highlighted)
