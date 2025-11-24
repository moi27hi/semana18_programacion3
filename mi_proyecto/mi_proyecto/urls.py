
from django.contrib import admin
from django.urls import path
from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio)
    path('guardar/',views.guardar_nombre),
    path('leer/',views.leer_nombre),
    path('eliminar/',views.eliminar_nombre),    
    path('limpiar/',views.limpiar_sesion),
    path('contador/',views.contador_visitas),
    path('login/',views.iniciar_sesion),
]
