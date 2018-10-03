from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('', include('django.contrib.auth.urls')),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), auth_views.LogoutView.next_page, name="logout"),

]

