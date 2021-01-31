from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # Question 모델의 조회 가능 속성
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)    # Question 모델과 QuestionAdmin 등록