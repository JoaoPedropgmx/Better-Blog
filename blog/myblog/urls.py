from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-details'),
    path('novo_post/', NewPost.as_view(), name='novo_post'),
    path('editar_post/<int:pk>', EditPost.as_view(), name='editar_post'),
    path('deletar_post/<int:pk>', DeletePost.as_view(), name='deletar_post')
]