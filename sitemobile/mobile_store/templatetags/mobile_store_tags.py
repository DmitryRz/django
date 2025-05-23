from django import template
import mobile_store.views as views

register = template.Library()

@register.inclusion_tag('mobile_store/category_select.html')
def filter_bars(current_category):
    return {
        'bars': views.FILTER_BAR,
        'current_category': current_category
    }