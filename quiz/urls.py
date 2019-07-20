from django.urls import path
from .views import question_detail

urlpatterns = [
    path('<int:question_id>', question_detail)
]