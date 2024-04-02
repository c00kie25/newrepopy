from django.urls import path
from tees.views import *
app_name='something'

urlpatterns=[
    path('tees/',tees,name='tees')

]