from django.urls import path, include
from .views import *

urlpatterns = [
    # path('login/', LoginUsuarioView.as_view(), name='login'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
]
