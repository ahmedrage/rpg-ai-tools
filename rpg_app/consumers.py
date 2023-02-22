import json
import threading
import requests
import os

import logging


from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        logger = logging.getLogger('testlogger')
        logger.info('This is a simple log message')
        self.accept()

    def disconnect(self, close_code):
        logger = logging.getLogger('testlogger')
        logger.info('This is a simple log message')

        # This method is called when the WebSocket is disconnected.
        # You can do any cleanup here.
        pass

    def receive(self, text_data):
        logger = logging.getLogger('testlogger')
        logger.info('This is a simple log message')

        data = json.loads(text_data)
        user_prompt = data['input']
        
        self.send(text_data= json.dumps({
            'response': "Generating response ..."
        }))

        def generate_response():
            print("generating response")
            prompt = "Generate a dungeons and dragons random roll table of 10 items for category {0}. Make sure to come up with creative names. Every item should be seperated with '<br>' and a number. Each items should have stats if appropriate.".format(user_prompt)
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

            # response = requests.post(url, headers=headers, json=data)
            print("got response")
            # text = response.json()['choices'][0]['text'].strip()
            text = "test"
            text.replace('\n', '<br>')
            print(repr(text))
            self.send(text_data= json.dumps({
                'response': text
            }))

        threading.Thread(target=generate_response).start()


        # self.send(text_data=json.dumps({
        #     'response': response
        # }))
