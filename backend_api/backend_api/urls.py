"""backend_api URL Configuration

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

"""
http post http://127.0.0.1:8000/api/token/ username=admin password=admin
 http http://127.0.0.1:8000/api/vendors/ "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzYwNjA2LCJpYXQiOjE3MjUzNjAzMDYsImp0aSI6ImVlMTc5MDgyNDc1NTQ2NjM4Njk3YjUzNjIwNmU4ZmZiIiwidXNlcl9pZCI6MX0.FSmPoAMh8S2EGrg_FDliowpP3d6pXIrvSxCxwjCTGFk"
  http http://127.0.0.1:8000/api/toekn/ refresh=refresh toekn here
"""
from django.contrib import admin
from backend_api import settings
from django.conf.urls.static import static
from django.urls import path,include
import main
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('main.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

