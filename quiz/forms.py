from django import forms
from .models import BooleanQuestionAnswer, MultipleChoiceQuestionAnswer, TheoryQuestionAnswer, MultipleChoiceQuestion


class BooleanQuestionForm(forms.ModelForm):
    class Meta:
        model = BooleanQuestionAnswer
        fields = ['answer']

class MultipleChoiceQuestionForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceQuestionAnswer
        fields = ['answer']

    def __init__(self, question_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ans_queryset = MultipleChoiceQuestion.objects \
            .get(question_number=question_id).options.all()
        self.fields['answer'].queryset = ans_queryset

# class MultipleChoiceQuestionForm(forms.Form):
    

class TheoryQuestionForm(forms.ModelForm):
    class Meta:
        model = TheoryQuestionAnswer
        fields = ['answer']