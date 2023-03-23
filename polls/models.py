import datetime

from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    IntegerField,
    UniqueConstraint
)
from django.utils import timezone


class Question(Model):
    question_text: CharField = CharField(max_length=200)
    pub_date: DateTimeField = DateTimeField('date published')

    def __str__(self) -> str:
        return str(self.question_text)

    def was_published_recently(self) -> bool:
        now: datetime = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        constraints: list[UniqueConstraint] = [
            UniqueConstraint(fields=['question_text'], name='unique_question')
        ]

class Choice(Model):
    question: ForeignKey = ForeignKey(Question, on_delete=CASCADE)
    choice_text: CharField = CharField(max_length=200)
    votes: IntegerField = IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choice_text)

    class Meta:
        constraints: list[UniqueConstraint] = [
            UniqueConstraint(fields=['question', 'choice_text'], name='unique_choice_per_question')
        ]
