from django.db import models

class Question(models.Model):
    question_text = models.CharFields(max_length=200)
    pub_date= models.DateTimeField('date_published')

class Chioce(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharFields(max_length=200)
    votes = models.IntegerFields(defaul=0)
