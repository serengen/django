from django.contrib import admin

from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from products.views import ProductListView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('users/login', views.login_view, name='login'),
    path('users/logout', views.logout_view, name='logout'),
    path('users/register', views.register_view, name='register'),
    path('admin/', admin.site.urls),
    path('products/',include('products.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)