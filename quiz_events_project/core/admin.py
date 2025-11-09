from django.contrib import admin
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event

# Quiz Admin
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

# Question Admin
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'quiz', 'question_type', 'created_at')
    list_filter = ('quiz', 'question_type')
    search_fields = ('text',)

# Answer Admin
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('text',)

# UserSubmission Admin
@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quiz', 'score', 'submitted_at')
    list_filter = ('quiz', 'submitted_at')
    search_fields = ('user__username',)

# UserAnswer Admin
@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'submission', 'question', 'answer', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('submission__user__username', 'question__text', 'answer__text')

# Event Admin
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description')
