from django.urls import path
from . import views

app_name = 'quiz'  # Ensure you have this if you're using a namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_quiz, name='start_quiz'),  # Ensure this path is named 'start_quiz'
    path('question/', views.get_question, name='question'),
    path('submit/', views.submit_answer, name='submit'),
    path('results/', views.quiz_results, name='results'),
]
