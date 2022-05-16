from django.db import models

# Create your models here.
'''
	질문과 답변을 하는 게시판 서비스
    @__str__
	:param : self
	:return: models에 있는 내부 Field 타입들
'''
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    create_date = models.DateTimeField()