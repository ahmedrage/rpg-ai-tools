import os
import requests
from django.db import models

class Assistant(models.Model):
    TYPE_CHOICES = [
        ('language', 'language'),
        ('image', 'image')
    ]

    label = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    prompt_template = models.TextField()
    temperature = models.FloatField(default=1.0)
    max_tokens = models.IntegerField(default=1000)
    assistant_type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return self.label

    def generate_prompt(self, inputs: dict):
        return self.prompt_template.format(**inputs)
# NEEDTO CHANGE BACK
    def get_ai_response(self, prompt: str):
        raise NotImplementedError()

class LanguageAssistant(Assistant):
    class Meta:
        proxy = True

    def get_ai_response(self, prompt: str):
        api_key = os.environ.get("API_KEY")

        url = 'https://api.openai.com/v1/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': api_key
        }
        data = {
            'model': 'text-davinci-003',
            'prompt': prompt,
            'temperature': self.temperature,
            'max_tokens': self.max_tokens
        }

        try:
            print("sending request")
            response = requests.post(
                url, headers=headers, json=data, timeout=300)
            print(repr(response.json()['choices'][0]['text']))
        except Exception as ex:
            print("Failed to get response")
            print(repr(response.json()))
            print(ex)
            return "Sorry, something went wrong, please try again."
        return response.json()['choices'][0]['text'].strip()


class AssistantInput(models.Model):
    TYPE_CHOICES = [
        ('text', 'text'),
        ('number', 'number'),
        ('select', 'select')
    ]
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    select_options = models.CharField(max_length=255, blank=True)
    input_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='text')


    def __str__(self):
        return self.label
