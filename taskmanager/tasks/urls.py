from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('registration/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/logout/', logout_view, name='logout'),

]
