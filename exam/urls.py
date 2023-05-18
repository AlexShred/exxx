from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions




schema_view = get_schema_view(
   openapi.Info(
      title="News",
      default_version='alpha-0.0.1',
      description="This api for news companies",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="m@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

swagger_urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/', include('news.urls')),
] + swagger_urlpatterns