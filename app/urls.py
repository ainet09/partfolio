from django.urls import path 
from .views import HomeTemplateView, contact

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='hom'),
    path('', contact, name='contact'),

]
