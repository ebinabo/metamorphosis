from django.shortcuts import render, redirect
from .models import (
    BooleanQuestion, 
    MultipleChoiceQuestion, 
    TheoryQuestion
)
from .forms import (
    BooleanQuestionForm, 
    MultipleChoiceQuestionForm, 
    TheoryQuestionForm
)

# Create your views here.
def question_detail(request, question_id):
    boolean = BooleanQuestion.objects.all()
    multiple_choice = MultipleChoiceQuestion.objects.all()
    theory = TheoryQuestion.objects.all()

    if boolean.filter(question_number = question_id).exists():
        question = boolean.get(question_number=question_id)

        if request.method == 'POST':
            form = BooleanQuestionForm(request.POST)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.question_id = question_id
            instance.save()
        else:
            form = BooleanQuestionForm()


    elif multiple_choice.filter(question_number = question_id).exists():
        question = multiple_choice.get(question_number=question_id)

        if request.method == 'POST':
            form = MultipleChoiceQuestionForm(question.question_number, request.POST)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.question_id = question_id
            instance.save()
        else:
            form = MultipleChoiceQuestionForm(question.question_number)


    elif theory.filter(question_number = question_id).exists():
        question = theory.get(question_number=question_id)

        if request.method == 'POST':
            form = TheoryQuestionForm(request.POST)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.question_id = question_id
            instance.save()
        else:
            form = TheoryQuestionForm()


    else:
        return redirect('home')

    context = {
        'form': form,
        'q': question
    }

    return render(request, 'question_detail.html', context)
