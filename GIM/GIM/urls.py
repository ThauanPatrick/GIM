from django.conf.urls import url
from search.views import home
from core.views import reset
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^home/', home),
    url(r'^reset/', reset),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
