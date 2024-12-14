import random
from django.shortcuts import render, redirect
from .models import Question, UserSubmission

def start_quiz(request):
    """
    Starts a new quiz session by resetting the session data for answered questions and question order.
    """
    # Initialize a new quiz session ID (if not already present)
    if 'quiz_session_id' not in request.session:
        request.session['quiz_session_id'] = request.session.session_key  # or you can create a custom session ID if needed

    # Reset session data
    request.session['answered_questions'] = []  # List of answered questions (by ID)
    request.session['question_order'] = []  # Track the order of questions answered

    # Redirect to the first question of the quiz
    return redirect('quiz:question')


def get_question(request):
    """
    Fetches the next random question and assigns a serial number (index).
    """
    answered_questions = request.session.get('answered_questions', [])
    remaining_questions = Question.objects.exclude(id__in=answered_questions)
    
    if not remaining_questions:
        return redirect('quiz:results')  # If no questions left, go to results
    
    # Randomly select a question
    question = random.choice(remaining_questions)
    
    # Update session with answered question and its serial number
    question_order = request.session.get('question_order', [])
    question_order.append(question.id)
    request.session['question_order'] = question_order

    context = {
        'question': question,
        'serial_number': len(question_order),  # Serial number is the length of the question_order
    }
    return render(request, 'quiz/question.html', context)

def submit_answer(request):
    """
    Handles the submission of an answer to a question and updates the session data.
    """
    # Check if 'quiz_session_id' is in the session
    if 'quiz_session_id' not in request.session:
        # If it's not there, initialize it (though this case should ideally be handled when the quiz starts)
        request.session['quiz_session_id'] = request.session.session_key

    if request.method == 'POST':
        question_id = request.POST['question_id']
        selected_option = request.POST['option']
        question = Question.objects.get(id=question_id)
        is_correct = (selected_option == question.correct_option)

        # Store submission in the database
        UserSubmission.objects.create(
            question=question,
            submitted_option=selected_option,
            is_correct=is_correct,
            session_id=request.session['quiz_session_id']  # Use the session's quiz session ID
        )

        # Update session to mark the question as answered
        answered_questions = request.session.get('answered_questions', [])
        answered_questions.append(question.id)
        request.session['answered_questions'] = answered_questions

    return redirect('quiz:question')

def quiz_results(request):
    """
    Displays the quiz results, showing each question along with the user's answers and correctness.
    """
    session_id = request.session.get('quiz_session_id')  # Fetch the session ID from the session
    
    # Get all submissions for the current quiz session
    submissions = UserSubmission.objects.filter(session_id=session_id)

    # Create a list to hold unique submissions (filtering out duplicates)
    unique_submissions = []
    seen_questions = set()

    for submission in submissions:
        if submission.question.id not in seen_questions:
            unique_submissions.append(submission)
            seen_questions.add(submission.question.id)
    
    total_correct = len([s for s in unique_submissions if s.is_correct])
    total_incorrect = len([s for s in unique_submissions if not s.is_correct])
    
    # Pass to template
    context = {
        'submissions': unique_submissions,
        'total_correct': total_correct,
        'total_incorrect': total_incorrect,
        'question_order': request.session.get('question_order', [])
    }
    
    return render(request, 'quiz/results.html', context)



def index(request):
    return render(request, 'quiz/index.html')
