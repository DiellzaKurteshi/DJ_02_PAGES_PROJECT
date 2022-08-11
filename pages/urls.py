from django.urls import path
from .views import HomePageView, AboutPageView, Contact

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('contact/', Contact.as_view(), name = 'contact'),
]