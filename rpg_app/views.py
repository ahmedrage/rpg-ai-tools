import os
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.core import serializers
from django.http import HttpResponse

from .models import LanguageAssistant, AssistantInput

def convert_assistants_to_json(assistant_list):
    response_json = {}
    print(assistant_list)
    for assistant in assistant_list:
        assistant_json = {}
        assistant_inputs = assistant.assistantinput_set.all()
        for assistant_input in assistant_inputs:
            input_json= {
                'type': assistant_input.input_type,
                'label': assistant_input.label,
                'select_options': assistant_input.select_options
            }
            assistant_json[assistant_input.name] = input_json

        response_json[assistant.name] = assistant_json

    print(response_json)
    return response_json

class IndexVIew(generic.ListView):
    template_name = 'rpg_app/index.html'
    context_object_name = 'assistant_list'

    def get_queryset(self):
        return LanguageAssistant.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assistant_data = convert_assistants_to_json(self.get_queryset())
        print(assistant_data)
        context['assistant_data'] = assistant_data
        return context
