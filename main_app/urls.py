from django.urls import path
from . import views #el punto siginifica que de la carpeta donde estamos importar un archivo

urlpatterns = [
    path('', views.index)
]

