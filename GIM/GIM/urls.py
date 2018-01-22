from django.conf.urls import url
from core.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^', home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
