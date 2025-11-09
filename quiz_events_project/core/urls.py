from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import (
    UserSubmissionViewSet, QuizListAPIView, QuizDetailAPIView,
    EventListAPIView, EventDetailAPIView, QuizViewSet, QuestionViewSet,
    AnswerViewSet, UserAnswerViewSet, EventViewSet)
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# DRF router for ModelViewSets
router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quizzes')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'user-submissions', UserSubmissionViewSet, basename='user-submissions')
router.register(r'user-answers', UserAnswerViewSet, basename='user-answers')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    
    # API URLs
    
    # Quiz APIs
    path('api/quizzes/', QuizListAPIView.as_view(), name='api-quizzes'),
    path('api/quizzes/<int:pk>/', QuizDetailAPIView.as_view(), name='api-quiz-detail'),
    # Events APIs
    path('api/events/', EventListAPIView.as_view(), name='api-events'),
    path('api/events/<int:pk>/', EventDetailAPIView.as_view(), name='api-event-detail'),

    # Template URLs
    path('', views.home, name='home'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', views.quiz_attempt, name='quiz_attempt'),
    path('events/', views.events_list, name='events'),
    path('quizzes/result/<int:submission_id>/', views.quiz_result, name='quiz_result'),
    
    # Authentication
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Quiz History
    path('my-quizzes/', views.quiz_history, name='quiz_history'),

]

# Add all router-based API endpoints
# urlpatterns += router.urls
urlpatterns += [
    path('api/', include(router.urls)),
]
