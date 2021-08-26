from django.urls import path,include
from backend.views import *


urlpatterns = [
    path('res',func1,name='homepage'),
    path('res1',func2,name='homepage2')
]