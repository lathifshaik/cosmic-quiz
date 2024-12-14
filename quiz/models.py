from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('ART', 'Art'),
        ('ASTRONOMY', 'Astronomy'),
    ]
    
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

class UserSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submitted_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    is_correct = models.BooleanField()
    session_id = models.CharField(max_length=255, null=True)  # Allow null values
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Allow null values for existing rows

    def __str__(self):
        return f"Submission for question {self.question.id} - Session {self.session_id}"
