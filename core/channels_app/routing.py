from django.urls import path
from . import consumers

websockets_urlpatterns = [
    path('ws/sc/' , consumers.EchoConsumer.as_asgi()),
]