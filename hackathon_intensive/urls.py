"""hackathon_intensive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include
from extended_user.views import SignUp

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/password-change/', PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('accounts/password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', include('extended_user.urls'), name='signup'),
    path('reg/', SignUp.as_view(), name='reg'),
    path('users/', include('extended_user.urls')),
    path('events/', include('event.urls')),
    path('classes/', include('classes.urls')),
    path('reg_events/', include('reg_event.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
