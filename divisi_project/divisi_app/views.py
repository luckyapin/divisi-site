from typing import Any, Dict
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .models import *
from .utils import *
from .forms import *
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
    
class RegistrationUser(DataMixin, CreateView):
    form_class = RegistrationUserForm
    template_name = 'divisi_app/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class AddProduct(DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'divisi_app/AddProduct.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Добавление товара')
        return dict(list(context.items())  + list(c_def.items()))

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдна</h1>')