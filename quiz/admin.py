from django.contrib import admin
from .models import (
    BooleanQuestion, BooleanQuestionAnswer,
    MultipleChoiceQuestion, MultipleChoiceQuestionOption,
    TheoryQuestion
)

# Register your models here.
class BooleanQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)


MODELS = [
    {'model': BooleanQuestion, 'admin': BooleanQuestionAdmin},
    {'model': BooleanQuestionAnswer, 'admin': BooleanQuestionAdmin},
    {'model': MultipleChoiceQuestion},
    {'model': MultipleChoiceQuestionOption},
    {'model': TheoryQuestion},
]

for model in MODELS:
    if 'admin' in model.keys():
        admin.site.register(model['model'], model['admin'])
    else:
        admin.site.register(model['model'])