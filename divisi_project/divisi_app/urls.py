from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', Divisi_home.as_view(), name='home'),
    path('product/<int:product_id>/', Product.as_view(), name='product'),
    path('register/', RegistrationUser.as_view(), name='registration'),
]
