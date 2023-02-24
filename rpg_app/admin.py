from django.contrib import admin
from .models import Assistant, AssistantInput, LanguageAssistant

class AssistantInputInLine(admin.TabularInline):
    model = AssistantInput
    extra = 3

class AssistantAdmin(admin.ModelAdmin):
    inlines = [AssistantInputInLine]
    fields = ('label', 'name', 'prompt_template', 'temperature', 'max_tokens')

admin.site.register(LanguageAssistant, AssistantAdmin)
