from . import views
from django.urls import path


## URL Conf.
urlpatterns = [
    path('hello/', views.say_hello),
]
