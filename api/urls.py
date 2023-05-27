from django.urls import path, include
from .views import VideoElementViewSet, AudioFragmentViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('video', VideoElementViewSet)
routers.register('audio', AudioFragmentViewSet)


urlpatterns = [
    path('', include(routers.urls))
]

