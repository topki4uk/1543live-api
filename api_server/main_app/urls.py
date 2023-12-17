from django.urls import path
from .views import index, lessons


urlpatterns = [
    path('lessons', lessons),
    path('lessons/<str:group>/', lessons)
]
