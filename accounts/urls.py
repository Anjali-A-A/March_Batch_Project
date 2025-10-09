from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='shop:allProdCat'), name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),

]