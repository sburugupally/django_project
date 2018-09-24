from django.db import models

# Create your models here.
class wordinfo(models.Model):
    date =models.CharField(max_length=20)
    word_name = models.CharField(max_length=20)
    word_meaning = models.CharField(max_length=50)
    word_opposite = models.CharField(max_length=50)
    word_synonyms = models.CharField(max_length=50)
    word_usage = models.CharField(max_length=50)
    def __str__(self):
        return self.date+'-'+self.word_name+'-'+self.word_meaning+'-'+self.word_opposite+'-'+self.word_synonyms+'-'+self.word_usage

class mail(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    nation = models.CharField(max_length=10)

    def __str__(self):
        return self.name+'-'+self.email+'-'+self.nation


class datepicker(models.Model):

    date =models.DateField(max_length=20)
