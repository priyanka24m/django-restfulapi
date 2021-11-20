from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('all_users/', views.get_all_users, name='get_all_users'),
    path('get_user/<int:id>', views.get_single_user, name='get_single_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('search_user/', views.search_user, name='search_user'),
]