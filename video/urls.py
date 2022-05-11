"""media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from video import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# apps' urls
from apps.media import urls as video_urls
from apps.main_page import urls as mp_urls

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Video Landing Page API",
        default_version='v1',
        description="Video Landing API list",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# getting lists of urls
routeLists = (
    video_urls.routeList,
    mp_urls.routeList,
)
# Registering all urls from apps
router = routers.DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(route[0], route[1], basename=route[0])


urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Api Root

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)