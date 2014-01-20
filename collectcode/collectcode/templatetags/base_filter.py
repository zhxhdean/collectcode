#uft-*-coding:utf8-*-
import re
from django import template

register = template.Library()

@register.filter
def remove_html_tags(str_html):
    return re.compile('</?\w+[^>]*>').sub('',str_html)
