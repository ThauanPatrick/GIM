from django.conf.urls import url
from core.view_result import result
from GIM.views import  home
from core.view_reset import  reset
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^$', home),
    url(r'^result/', result),
    url(r'^reset/', reset),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
