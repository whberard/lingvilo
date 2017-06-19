from django.db import models

# Create your models here.
class Verb(models.Model):
    verb = models.CharField(max_length=30)
    translation = models.CharField(max_length=50, blank=True)
    is_transitive = models.BooleanField()

    def __str__(self):
        return self.verb


class Reason(models.Model):
    reason = models.CharField(max_length=50)

    def __str__(self):
        return self.reason


class End(models.Model):
    phrase = models.CharField(max_length=100)
    translation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.phrase


class Start(models.Model):
    phrase = models.CharField(max_length=100)
    translation = models.CharField(max_length=100, blank=True)
    why = models.ForeignKey(Reason, blank=True, null=True, on_delete=models.SET_NULL)
    ends = models.ManyToManyField(End, blank=True)


    def __str__(self):
        return self.phrase
