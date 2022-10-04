from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users.views import RegisterView, ProfileView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blogapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
