# core/api_views.py
from rest_framework import viewsets, generics
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event
from .serializers import (
    QuizSerializer, QuestionSerializer, AnswerSerializer,
    UserSubmissionSerializer, UserAnswerSerializer, EventSerializer
)

# ------------------------------
# Quiz APIs
# ------------------------------

# Full CRUD for quizzes
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

# Full CRUD for questions
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Full CRUD for answers
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# Read-only list of quizzes (optional if you want separate read API)
class QuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

# Retrieve quiz detail with questions (optional)
class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


# ------------------------------
# UserSubmission APIs
# ------------------------------

# Full CRUD for user submissions
class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer

# Full CRUD for user answers
class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer


# ------------------------------
# Event APIs
# ------------------------------

# Full CRUD for events
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Optional read-only endpoints
class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
