from django import template
import mobile_store.views as views
from mobile_store.models import Product

register = template.Library()

@register.inclusion_tag('mobile_store/category_select.html')
def filter_bars(current_category):
    bars = list(Product.objects.values("category").distinct())
    bars.insert(0, {'id': 0, 'category': 'Все категории'})
    bars_with_id = [{'id': idx, 'category': item['category']} for idx, item in enumerate(bars)]

    data = {
        'bars': bars_with_id,
        'current_category': current_category
    }
    return data