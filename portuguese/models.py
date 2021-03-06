from django.db import models
import datetime

# Create your models here.
class Verb(models.Model):
    verb = models.CharField(max_length=30)
    translation = models.CharField(max_length=50, blank=True)
    is_transitive = models.BooleanField()

    def __str__(self):
        return self.verb


class Word(models.Model):
    word = models.CharField(max_length=30)
    translation = models.CharField(max_length=100, blank=True)
    is_known = models.BooleanField()
    last_review = models.DateField(default=datetime.date(2000,1,1))

    def __str__(self):
        return self.word
