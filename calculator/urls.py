from django.urls import path
from . import views

urlpatterns = []

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_view, name='calculate'),
    path('<int:id>/result/', views.result_view, name='result'),
    path('<int:id>/pdf/', views.download_pdf, name='download_pdf'),
]