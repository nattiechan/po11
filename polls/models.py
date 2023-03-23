import datetime

from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, IntegerField
from django.utils import timezone


class Question(Model):
    question_text: CharField = CharField(max_length=200)
    pub_date: DateTimeField = DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(Model):
    question: ForeignKey = ForeignKey(Question, on_delete=CASCADE)
    choice_text: CharField = CharField(max_length=200)
    votes: IntegerField = IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
