from django.urls import path
from .views import CreateEmployeView,UpdateEmployeView,DeleteEmployeView,ListEmployeView
urlpatterns = [
    path("create/",CreateEmployeView.as_view(),name = "create"),
    path("update/<str:regid>/",UpdateEmployeView.as_view(),name = "Update"),
    path("list/",ListEmployeView.as_view(),name = "list"),
    path("delete/<str:regid>/",DeleteEmployeView.as_view(),name = "delete"),
    path("get/<str:regid>/",ListEmployeView.as_view(),name = "get")
    
]