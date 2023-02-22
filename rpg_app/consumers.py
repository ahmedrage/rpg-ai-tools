import json
import threading
import requests
import os

import logging


from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):

        # This method is called when the WebSocket is disconnected.
        # You can do any cleanup here.
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        user_prompt = data['input']
        
        self.send(text_data= json.dumps({
            'loading': True
        }))

        def generate_response():
            prompt = "Generate a dungeons and dragons random roll table of 10 items for category {0}. Make sure to come up with creative names. The list should be formatted as: 'n. Item name - Description - stats <br>'. Make sure to add the <br> tag.".format(user_prompt)
            api_key = os.environ.get("API_KEY")

            url = 'https://api.openai.com/v1/completions'
            headers = {
                'Content-Type': 'application/json',
                'Authorization': api_key
            }
            data = {
                'model': 'text-davinci-003',
                'prompt': prompt,
                'temperature': 1,
                'max_tokens': 1000
            }

            response = requests.post(url, headers=headers, json=data)
            print("got response")
            print(repr(response.json()['choices'][0]['text']))
            text = response.json()['choices'][0]['text'].strip()
            print(repr(text))
            text.replace('\n', '<br>')
            self.send(text_data= json.dumps({
                'response': text,
                'loading': False
            }))

        threading.Thread(target=generate_response).start()


        # self.send(text_data=json.dumps({
        #     'response': response
        # }))
