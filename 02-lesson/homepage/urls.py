from django.urls import path
from .views import homePageView, goodbyeView

urlpatterns = [
    path('', homePageView, name='home'),
    path('/bye', goodbyeView, name='bye')
]