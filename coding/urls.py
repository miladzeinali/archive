from django.urls import path
from .views import *

app_name = 'coding'
urlpatterns = [
    path('',CategoryView,name='category'),
    path('samelevel/<int:id>/',AddSameLevel,name='addsamelevel'),
    path('get_parent_node/',get_parent_node,name='get-parent-node'),
]