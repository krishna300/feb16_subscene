

from django.urls import path

from .views import *

urlpatterns = [
   
     path('',PostListView.as_view(),name="list"),
     path('detail/<int:post_id>',detail,name='detail'),

]