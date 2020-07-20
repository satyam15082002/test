
from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name="home"),  
path('create',views.create,name="create"),  
 path('creategroup',views.create_group,name="creategroup"),
  path('<int:id>',views.ingroup,name="insidegroup"), 
  path('search',views.search,name="search"),   
  path('add/<int:group_id>',views.add,name="add"),    
  path('addmsg/<int:g_id>',views.addmsg,name="addmsg"), 
  path('loadmsg/<int:g_id>',views.loadmsg,name="loadmsg"), 
  path('delete/<int:g_id>',views.delete,name="delete"), 
]