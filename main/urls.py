from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog_post_list, name='blog_post_list'),
    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('post/new/', views.blog_post_new, name='blog_post_new'),
    path('post/<int:pk>/edit/', views.blog_post_edit, name='blog_post_edit'),
    path('post/<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),
    path('chatbot/', views.chatbot_index, name='chatbot_index'),
    path('chatbot/get_response/', views.get_chatbot_response, name='get_chatbot_response'),
]