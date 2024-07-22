from django.db import models
from django.contrib.auth.models import User


# 질문모델
class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question')  # 글쓴이
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 내용
    create_date = models.DateTimeField()  # 작성일시
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일시
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천수

    def __str__(self):
        return self.subject


# 답변모델
class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


# 대댓 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)
