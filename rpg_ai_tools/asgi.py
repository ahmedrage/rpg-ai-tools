import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from rpg_app.consumers import MyConsumer
from django.urls import path
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rpg_ai_tools.settings')
django.setup()
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("my_consumer/", MyConsumer.as_asgi()),
            ]
        )
    ),
})
