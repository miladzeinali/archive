from django.urls import path
from .views import *

app_name = 'coding'
urlpatterns = [
    path('category',CategoryView,name='category'),
    path('samelevel/<int:id>/',AddSameLevel,name='addsamelevel'),
]