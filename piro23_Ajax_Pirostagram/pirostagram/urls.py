from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like/', views.toggle_like, name='toggle_like'),
    path('comment/add/', views.add_comment, name='add_comment'),
    path('comment/delete/', views.delete_comment, name='delete_comment'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
