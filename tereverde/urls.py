from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Tere Verde Administração" 
admin.site.site_title = "Tere Verde Admin Portal" 
admin.site.index_title = "Bem-vindo ao Portal de Administração Tere Verde"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
