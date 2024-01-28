
from django.urls import path
from . import views
app_name = 'food'

urlpatterns = [
    
   path('',views.IndexClassView.as_view(),name="index"),
   path('update/<int:id>/',views.update_item,name="update"),
   path('delete/<int:pk>/',views.delete_item,name="delete"),
   path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
   path('item/',views.item,name="item"),
   # add to item
   path('add/',views.CreateItem.as_view(),name="create_item"),
  
   
   
  
    
               
]

