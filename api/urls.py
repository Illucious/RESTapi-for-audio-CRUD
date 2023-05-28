from django.urls import path, include
#from .views import VideoElementViewSet, AudioFragmentViewSet
from  . import views
from rest_framework import routers

routers = routers.DefaultRouter()
"""routers.register('video', VideoElementViewSet)
routers.register('audio', AudioFragmentViewSet)"""


urlpatterns = [
    path('', include(routers.urls)),
    path('audio-elements/', views.audio_elements, name='audio_elements'),
    path('audio-fragments/<int:fk>/', views.audio_fragments, name='audio_fragments'),
]

