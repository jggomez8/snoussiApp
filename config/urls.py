"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0.3/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings as setting
from core.home.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('security/', include('core.security.urls')),
    path('login/', include('core.login.urls')),
    path('user/', include('core.user.urls')),
    path('rrhh/', include('core.rrhh.urls')),
]

if setting.DEBUG:
    urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)
