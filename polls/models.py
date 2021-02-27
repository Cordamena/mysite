from django.db import models

# Модель для обработки вопроса
class Question(models.Model):
    text = models.CharField(max_length=1000)
    pub_Date = models.DateTimeField("date published")
    #в момент конверации в str()
    def __str__(self):
        return self.text
class Choice(models.Model):
    # связываем question и choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
    #В момент конвертации в str()
    def __str__(self):
        return self.text