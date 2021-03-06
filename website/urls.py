from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = 'webapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]

handler404 = 'webapp.views.custom_page_not_found_view'

urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)