from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView, FormView

from .models import *
from .utils import *
# Create your views here.

class Divisi_home(DataMixin, ListView):
    model = Products
    template_name = 'divisi_app/catalog.html'
    context_object_name = 'Products'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', photos=Photos.objects.all())
        return dict(list(context.items())  + list(c_def.items()))
    
    def get_queryset(self):
        return Products.objects.all()

class Product(DataMixin, DetailView):
    model = Products
    template_name = 'divisi_app/product.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'], photos=Photos.objects.filter(product__pk=self.kwargs['product_id']))
        print(dict(list(context.items())  + list(c_def.items())))
        return dict(list(context.items())  + list(c_def.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдна</h1>')