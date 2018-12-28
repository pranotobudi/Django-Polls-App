from django.urls import path
from . import views
polls_urlpatterns = [
    path('', views.index, name="index" ),
]