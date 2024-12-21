"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # Pre-built views for token generation (for access and refresh tokens) and to refresh the access token

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"), # Create/register a new user, also adding the name "register" allows us to refer to the path by name in many places in the code
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), # Generate access and refresh tokens
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # Refresh the access token
    path("api-auth/", include("rest_framework.urls")), # Built-in views for login and logout
    path("api/", include("api.urls")), # Whenever we go to api/ and it isn't one of the ones above, we'll take the remainder of the path and forward it to api.urls
]
