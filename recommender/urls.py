from django.urls import path
from . import views

urlpatterns = [

    # ================= PUBLIC =================
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ================= USER =================
    path('predict/', views.predict_view, name='predict'),
    path('profile/', views.user_profile_view, name='profile'),
    path('history/', views.user_history_view, name='history'),
    path('change-password/', views.user_change_password_view, name='change_password'),
    # urls.py

path(
    'delete-prediction/<int:pk>/',
    views.user_delete_predictions,
    name='user_delete_predictions'
),

    path(
        'delete-prediction/<int:pk>/',
        views.user_delete_predictions,
        name='user_delete_predictions'
    ),

    # ================= ADMIN AUTH =================
    path(
        'admin-login/',
        views.admin_login_view,
        name='admin_login'
    ),

    path(
        'admin-register/',
        views.admin_register,
        name='admin_register'
    ),

    path(
        'forgot-password/',
        views.forgot_password,
        name='forgot_password'
    ),

    path(
        'admin-logout/',
        views.admin_logout_view,
        name='admin_logout'
    ),

    # ================= ADMIN PANEL =================
    path(
        'admin-dashboard/',
        views.admin_dashboard_view,
        name='admin_dashboard'
    ),

    path(
        'admin-users/',
        views.admin_view_users,
        name='admin_users'
    ),

    path(
        'admin-delete-user/<int:pk>/',
        views.admin_delete_user,
        name='admin_delete_user'
    ),

    path(
        'admin-predictions/',
        views.admin_predictions,
        name='admin_predictions'
    ),

    path(
        'admin-delete-prediction/<int:pk>/',
        views.admin_delete_prediction,
        name='admin_delete_prediction'
    ),
]