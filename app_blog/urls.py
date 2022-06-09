
from django.urls import path
from . import views

app_name='app_blog'

urlpatterns = [
    
    path('',views.BlogList.as_view(),name='blog_list'),
    path('write/',views.CreateBlog.as_view(),name='create_blog'),
    path('details/<str:slug>/',views.blog_details,name='blog_details'),
    path('MyBlog',views.MyBlog.as_view(),name='MyBlog'),
    path('edit/<pk>/',views.UpdateBlog.as_view(),name='edit_blog'),
    


]
