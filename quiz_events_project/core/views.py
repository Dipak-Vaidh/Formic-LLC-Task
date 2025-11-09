from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Quiz, Event, Question, Answer , UserSubmission, UserAnswer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from .models import UserSubmission

# Home Page
@login_required
def home(request):
    return render(request, "core/home.html")

# Quiz List Page
@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "core/quiz_list.html", {"quizzes": quizzes})

@login_required
def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == "POST":
        score = 0

        submission = UserSubmission.objects.create(
            quiz=quiz,
            user=request.user,
            score=0
        )

        for question in questions:
            user_answer = request.POST.get(f"question_{question.id}")
            correct = False

            if question.question_type == "MCQ":
                if user_answer:
                    answer_obj = Answer.objects.get(id=int(user_answer))
                    correct = answer_obj.is_correct
                    UserAnswer.objects.create(
                        submission=submission,
                        question=question,
                        answer=answer_obj.text,
                        is_correct=correct
                    )
            elif question.question_type == "TEXT":
                answer_obj = Answer.objects.filter(question=question, text__iexact=user_answer).first()
                if answer_obj:
                    correct = answer_obj.is_correct
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    answer=user_answer,
                    is_correct=correct
                )

            if correct:
                score += 1

        submission.score = score
        submission.save()
        return redirect("quiz_result", submission_id=submission.id)

    return render(request, "core/quiz_attempt.html", {"quiz": quiz, "questions": questions})

# Events Page
@login_required
def events_list(request):
    events = Event.objects.all()
    return render(request, "core/events.html", {"events": events})

@login_required
def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()  # ✅ correct

    if request.method == "POST":
        score = 0

        # Create UserSubmission using the logged-in user
        submission = UserSubmission.objects.create(
            quiz=quiz,
            user=request.user,  # ✅ no 'user_name', use logged-in user
            score=0
        )

        for question in questions:
            user_answer = request.POST.get(f"question_{question.id}")
            correct = False

            if question.question_type == "MCQ":
                if user_answer:
                    answer_obj = Answer.objects.get(id=int(user_answer))
                    correct = answer_obj.is_correct
                    # Store answer text
                    UserAnswer.objects.create(
                        submission=submission,
                        question=question,
                        answer=answer_obj.text,
                        is_correct=correct
                    )
            elif question.question_type == "TEXT":
                # Check if user text matches any correct answer
                answer_obj = Answer.objects.filter(question=question, text__iexact=user_answer).first()
                if answer_obj:
                    correct = answer_obj.is_correct
                    answer_text = answer_obj.text
                else:
                    answer_text = user_answer or ""

                # Store text answer
                UserAnswer.objects.create(
                    submission=submission,
                    question=question,
                    answer=answer_text,
                    is_correct=correct
                )

            if correct:
                score += 1

        # Update total score
        submission.score = score
        submission.save()

        return redirect("quiz_result", submission_id=submission.id)

    return render(request, "core/quiz_attempt.html", {"quiz": quiz, "questions": questions})

@login_required
def quiz_result(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id)
    answers = submission.useranswer_set.all()
    total_questions = submission.quiz.questions.count()  # <-- FIXED

    return render(request, "core/quiz_result.html", {
        "submission": submission,
        "answers": answers,
        "total_questions": total_questions
    })

    
@login_required    
def events_list(request):
    events = Event.objects.all().order_by('date')  # sort by date
    return render(request, "core/events.html", {"events": events})

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/sign_up.html', {'form': form})

# logout
def user_logout(request):
    logout(request)
    return redirect('home') 

@login_required
def quiz_history(request):
    submissions = UserSubmission.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'core/quiz_history.html', {'submissions': submissions})