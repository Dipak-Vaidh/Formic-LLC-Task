from rest_framework import serializers
from .models import Quiz, Question, Answer,  UserSubmission, UserAnswer, Event

# Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')

# Question Serializer
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'text', 'question_type', 'answers')

# Quiz Serializer
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'questions')
     
# User Answer Serializer 
class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id', 'question', 'answer', 'is_correct')

# User Submission Serializer
class UserSubmissionSerializer(serializers.ModelSerializer):
    answers = UserAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = UserSubmission
        fields = ('id', 'quiz', 'user', 'score', 'submitted_at', 'answers')

# Event Serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'date', 'location')

