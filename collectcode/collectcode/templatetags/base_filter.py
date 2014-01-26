#uft-*-coding:utf8-*-
import re
from django import template
from django.utils.safestring import mark_safe
from django.utils.text import truncate_html_words

register = template.Library()

@register.filter
def remove_html_tags(str_html):
    return re.compile('</?\w+[^>]*>').sub('',str_html)


@register.filter
def truncatewords_html_remove_end(value,arg):
    arg_list = arg.split(',')
    try:
        length = int(arg_list[0])
    except ValueError:
        return value
    return mark_safe(truncate_html_words(value,length,''))
