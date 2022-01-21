from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from .linkmaker import link

urlpatterns = [

    path('admin/', admin.site.urls),

    path('redirect_link', RedirectView.as_view(url=link)),

    path('', include('app.urls'))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
