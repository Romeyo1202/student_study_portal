from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from dashboard import views as dash_views   #for differciate kaga
from django.contrib.auth import views as auth_views  # login form create pannum bothu ithu kudukanum
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    
    path('register/', dash_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('profile/', dash_views.profile, name='profile'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='dashboard/login.html'), name='logout'),
    #path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    #path('logout/', dash_views.logout, name='logout'),
    path('logout_user/', dash_views.logout_user, name='logout')

]
