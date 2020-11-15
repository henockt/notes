from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('new/', views.new, name="new"),
    path('shared/<str:note_id>', views.shared, name="shared")
]