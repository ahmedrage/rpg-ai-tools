import os
import json
import threading
import requests

import logging


from channels.generic.websocket import WebsocketConsumer
from .models import Assistant, AssistantInput, LanguageAssistant


class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):

        # This method is called when the WebSocket is disconnected.
        # You can do any cleanup here.
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        print("RECIEVING DATA")
        print(data)
        assistant_name = data['assistant_name']

        self.send(text_data=json.dumps({
            'loading': True,
            'assistant_name': assistant_name
        }))

        del data['assistant_name']

        assistant = LanguageAssistant.objects.get(name=assistant_name)
        prompt = assistant.generate_prompt(data)
        response = assistant.get_ai_response(prompt)

        self.send(text_data=json.dumps({
            'response': response,
            'loading': False,
            'assistant_name': assistant_name
        }))