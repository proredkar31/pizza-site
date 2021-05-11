
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include('pizza.urls')),
]

handler404='pizza.views.error_404_view'
handler505='pizza.views.error_404_view'