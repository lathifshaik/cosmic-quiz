from django.contrib import admin
from .models import Question, UserSubmission

admin.site.register(Question)
admin.site.register(UserSubmission)
