from django.db import models
from django.contrib.auth.models import User

# Quiz Model
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Question Model
class Question(models.Model):
    QUESTION_TYPES = (
        ('MCQ', 'Multiple Choice'),
        ('TF', 'True / False'),
        ('TEXT', 'Text Input'), 
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]  

# Answer Model (Stores correct answers for a Question)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

# UserSubmission Model (Stores the user's overall quiz attempt details)
class UserSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} ({self.score})"

# UserAnswer Model (Stores the specific answer for each question in a submission)
class UserAnswer(models.Model):
    # This is the parent link, the related_name 'user_answers' is the correct accessor.
    submission = models.ForeignKey(UserSubmission, on_delete=models.CASCADE, related_name='user_answers') 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    # FIX: Made nullable (null=True, blank=True) to handle TEXT answers that don't match 
    # a pre-defined Answer object, preventing database errors.
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True) 
    
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.submission.user.username} - {self.question.text[:30]}"

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title} ({self.date})"