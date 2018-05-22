import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
"""Each model is represented by a class that subclasses 
django.db.models.Model. Each model has a number of class variables, 
each of which represents a database field in the model."""

class Question(models.Model):
    """Each field is represented by an instance of a Field class – 
    e.g., CharField for character fields and DateTimeField for date 
    times. This tells Django what type of data each field holds.
    
    The name of each Field instance (e.g. question_text or pub_date)
    is the field’s name, in machine-friendly format. You’ll use this 
    value in your Python code, and your database will use it as the 
    column name."""
    question_text = models.CharField(max_length=200)
    """You can use an optional first positional argument to a Field to 
    designate a human-readable name.  In this example, we’ve only 
    defined a human-readable name for Question.pub_date."""
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """Finally, note a relationship is defined, using ForeignKey. That 
    tells Django each Choice is related to a single Question. Django 
    supports all the common database relationships: many-to-one, 
    many-to-many, and one-to-one."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    """Some Field classes have required arguments. CharField, for 
    example, requires that you give it a max_length"""
    choice_text = models.CharField(max_length=200)
    """A Field can also have various optional arguments; 
    in this case, we’ve set the default value of votes to 0."""
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text