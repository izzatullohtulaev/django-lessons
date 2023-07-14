from django.urls import path
from .views import HomePageView, AboutPageView, CareerPageView, RussianPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('career/', CareerPageView.as_view(), name='career'),
    path('russian/', RussianPageView.as_view(), name='russian')
]