from .models import *
from django.db.models import Count

menu = [
    {'title': 'Каталог', 'url_name': 'home'},
    {'title': 'Корзина', 'url_name': 'home'},
    {'title': 'Профиль', 'url_name': 'home'},
    {'title': 'Регистрация', 'url_name': 'registration'},
    {'title': 'Добавить товар', 'url_name': 'addproduct'}
    ]

class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        
        cats = Category.objects.annotate(Count('products'))
            
        
        user_menu = menu.copy() 
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        
        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context