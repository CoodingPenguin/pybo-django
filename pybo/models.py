from django.db import models

# Question 모델 정의
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    # 출력시 객체 이름이 아닌 제목(subject) 출력
    def __str__(self):
        return self.subject


# Answer 모델 정의
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()