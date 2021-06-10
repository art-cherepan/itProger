from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as mainViews
from users import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name='reg'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile/', userViews.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
