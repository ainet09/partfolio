from django.urls import path 
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='hom'),
    # path('#contact/', ContactModelView.as_view(), name='contact'),

]
