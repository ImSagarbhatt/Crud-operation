from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('edit/<int:pk>', views.editview, name="todoedit"),
    path('delete/<int:pk>', views.deleteview, name="tododelete"),
]
