from django.urls import path
from .views import ges_list


urlpatterns = [
    path('', ges_list, name='index'),
]