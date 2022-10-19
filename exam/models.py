from email.policy import default
from hashlib import blake2b
from operator import mod
from re import T
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator
from sqlalchemy import null


# Create your models here.

class QuestionSet(models.Model):
    set_name = models.CharField(max_length=100)
    set_slug = models.SlugField(max_length = 250, null = True, blank = True)
    enable_negative_marking = models.BooleanField(default=False)
    negative_marking_percentage = models.IntegerField()
    idealtimetocomplete = models.IntegerField()



class Question(models.Model):
    QUESTIONTYPE_CHOICES = (
        ('MCQWithRadio', 'MCQWithRadio'),
        ('MCQWithCheckBox', 'MCQWithCheckBox'),
        ('Matrix', 'Matrix'),
    ) 
    id_questionset = models.ForeignKey("QuestionSet", on_delete=models.CASCADE,null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    question_image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['jpg','png'])])
    question_type = models.CharField(max_length=100, choices=QUESTIONTYPE_CHOICES,default='MCQWithRadio')
    question_order = models.IntegerField(null=True,blank=True)
    question_marks = models.IntegerField(default=1)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    option_image = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['jpg','png'])])
    correct_answer = models.CharField(max_length=100)
    duration = models.IntegerField(null=True, blank=True)

class Clock(models.Model):
    time = models.IntegerField()
    flag = models.BooleanField(default=False)

class Solution(models.Model):
    number = models.IntegerField()
    username = models.CharField(max_length=100)
    questions = models.CharField(max_length=400, blank=True)
    solution = models.CharField(max_length=400, blank=True)
    class Meta:
        unique_together = (('number', 'username'),)


class GroupQuestion(Question):
    pass


class groupInlineQuestions(models.Model):
    id_group_question = models.ForeignKey("GroupQuestion", on_delete=models.CASCADE)
    id_question = models.ForeignKey("Question", on_delete=models.CASCADE,related_name='related_question')
    question_order = models.IntegerField()
    question_marks = models.IntegerField()

        


