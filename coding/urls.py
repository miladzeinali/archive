from django.urls import path
from .views import *

app_name = 'coding'
urlpatterns = [
    path('',Home,name='home'),
    path('category',CategoryView,name='category'),
    path('samelevel/<int:id>/',AddSameLevel,name='addsamelevel'),
    path('area/<int:id>/',AreaView,name='area'),
    path('MES/<int:id>/',ME,name='mes'),
]