from django.urls import path

from testsite.views import *



urlpatterns = [
    # path('', HomeTests.as_view(), name='home'),
    path('', index, name='index'),
]