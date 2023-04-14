
from django.urls import path
from .views import BlogListView,CreateBlogView

app_name='blog'

urlpatterns=[
    path('',BlogListView.as_view(),name='home'),
    path('create/',CreateBlogView.as_view(),name='create')
    
]