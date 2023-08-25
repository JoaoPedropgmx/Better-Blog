from django.urls import path, include
from .views import HomeView, PostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post-details')
]