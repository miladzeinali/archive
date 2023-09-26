from django.urls import path
from .views import *

app_name = 'coding'
urlpatterns = [
    path('',CategoryView,name='category'),
    path('addingcontrol/<obj>/',AddRedirect,name='addingredirect'),
    path('samelevel/',AddSameLevel,name='addsamelevel'),
    path('get_parent_node/',get_parent_node,name='get-parent-node'),
    path('caption/',Caption,name='caption'),
    path('updatecaption/',UpdateCaption,name='updatecaption'),
    path('search/',Search,name='search'),
    path('addcontrol/',AddingControl,name='addcontrol')
]