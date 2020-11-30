from django.urls import path
from api import views

app_name = "api"

urlpatterns = [
    path("v1/lista_medicos/", views.MedicoList.as_view(), name="lista_medicos"),
    path("v1/detail_medico/<int:pk>/", views.MedicoDetail.as_view(), name="detail_medico"),
]
