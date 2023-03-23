from datetime import datetime
from django.db import IntegrityError

from django.test import TestCase
from django.utils import timezone

from .models import Question, Choice

# Ideally there should be more test coverage
# The primary goal of these tests is to ascertain
# the question and choice text are unique
class QuestionModelTest(TestCase):
    QUESTION_TEXT: str = 'foo'
    CHOICE_TEXT_1: str = '123'

    @classmethod
    def setUpTestData(cls) -> None:
        Question.objects.create(
            question_text=cls.QUESTION_TEXT,
            pub_date=timezone.make_aware(datetime(2022, 1, 1))
        )
        Question.objects.create(question_text="bar", pub_date=timezone.now())
        question: Question = Question.objects.get(question_text=cls.QUESTION_TEXT)
        question.choice_set.create(choice_text=cls.CHOICE_TEXT_1, votes=0)
        question.choice_set.create(choice_text='456', votes=0)

    def test_insert_new_question_successful(self):
        text: str = 'hi'
        Question.objects.create(question_text=text, pub_date=timezone.now())
        self.assertEqual(Question.objects.count(), 3)
        self.assertEqual(Question.objects.get(question_text=text).question_text, text)

    def test_insert_new_choice_text_successful(self):
        question_text: str = 'world'
        choice_text: str = '789'
        votes: str = 3
        Question.objects.create(question_text=question_text, pub_date=timezone.now())
        question: Question = Question.objects.get(question_text=question_text)
        question.choice_set.create(choice_text=choice_text, votes=votes)
        self.assertEqual(Choice.objects.count(), 3)
        self.assertEqual(Choice.objects.get(choice_text=choice_text).votes, votes)
   
    def test_insert_duplicate_question_text_fails(self):
        with self.assertRaises(IntegrityError):
            Question.objects.create(question_text=self.QUESTION_TEXT, pub_date=timezone.now())
  
    def test_insert_duplicate_choice_text_fails(self):
        with self.assertRaises(IntegrityError):
            question: Question = Question.objects.get(question_text=self.QUESTION_TEXT)
            question.choice_set.create(choice_text=self.CHOICE_TEXT_1, votes=0)
