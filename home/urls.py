from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Numero1.as_view(), name="numero1.10"),
    path('numero2.10/', views.Numero2.as_view(), name="numero2.10"),
    path('numero3.10/', views.Numero3.as_view(), name="numero3.10"),
    path('numero4.10/', views.Numero4.as_view(), name="numero4.10"),
    path('numero5.10/', views.Numero5.as_view(), name="numero5.10"),
    path('numero6.10/', views.Numero6.as_view(), name="numero6.10"),
    path('numero7.10/', views.Numero7.as_view(), name="numero7.10"),
    path('numero8.10/', views.Numero8.as_view(), name="numero8.10"),
    path('numero9.10/', views.Numero9.as_view(), name="numero9.10"),
    path('numero10.10/', views.Numero10.as_view(), name="numero10.10"),
]
