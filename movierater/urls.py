from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import wszystkie_filmy
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

urlpatterns = [
    path('', wszystkie_filmy),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
