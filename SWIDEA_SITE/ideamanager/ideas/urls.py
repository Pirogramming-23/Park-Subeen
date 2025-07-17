from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    # Idea
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('idea/<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('idea/<int:pk>/adjust_interest/', views.adjust_interest, name='adjust_interest'),

    # DevTool
    path('devtools/', views.devtool_list, name='devtool_list'),
    path('devtool/create/', views.devtool_create, name='devtool_create'),
    path('devtool/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtool/<int:pk>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtool/<int:pk>/delete/', views.devtool_delete, name='devtool_delete'),
]
