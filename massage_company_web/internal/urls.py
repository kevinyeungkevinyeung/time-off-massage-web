from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    # path('upload/', views.image_upload_view)
]