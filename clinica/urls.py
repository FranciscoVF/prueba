from django.urls import path

from clinica import views

app_name = "clini"

urlpatterns = [
    path('list/', views.List.as_view(), name="list"),
    path('detail/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('newcategory/', views.NewCategory.as_view(), name= "newcategory"),
    path('update/<int:pk>/', views.UpdateCategory.as_view(), name="update"),
    path('delete_category/<int:pk>/', views.DeleteCategory.as_view(), name="delete_category"),

    path('list_subcategory/', views.ListSubCategory.as_view(), name="list_subcategory"),
    path('detail_subcategory/<int:pk>/', views.DetailSubCategory.as_view(), name="detail_subcategory"),
    path('newsubcategory/', views.NewSubCategory.as_view(), name= "newsubcategory"),
    path('update_subcategory/<int:pk>/', views.UpdateSubCategory.as_view(), name="update_subcategory"),
    path('delete_subcategory/<int:pk>/', views.DeleteSubCategory.as_view(), name="delete_subcategory"),

    path('trauma/', views.medicoTraumatologia,name="trauma"),
    path('ws_medicos/', views.wsmedicos, name="ws_medicos"),
    path('ws_medicos2/', views.wsmedicos2, name="ws_medicos2"),
]
