from django.db import models

# Create your models here.
class Verb(models.Model):
    verb = models.CharField(max_length=30)
    translation = models.CharField(max_length=50, blank=True)
    is_transitive = models.BooleanField()

    def __str__(self):
        return self.verb


