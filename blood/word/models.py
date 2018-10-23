from django.db import models
from django.utils.html import linebreaks


# Create your models here.
class wordinfo(models.Model):
    date =models.CharField(max_length=20)
    word_name = models.CharField(max_length=200)
    word_Transliteration=models.CharField(max_length=100)
    word_meaning = models.CharField(max_length=500)
    word_synonyms = models.CharField(max_length=500)
    word_english=models.CharField(max_length=100)
    word_usage = models.CharField(max_length=1000)
    quote=models.CharField(max_length=2000)
    poem=models.CharField(max_length=2000)
    def __str__(self):
        return self.date+'-'+self.word_name+'-'+self.word_Transliteration+'-'+self.word_meaning+'-'+self.word_synonyms+'-'+self.word_english+'-'+self.word_usage+'-'+self.quote+'-'+linebreaks(self.poem)

class mail(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    nation = models.CharField(max_length=10)

    def __str__(self):
        return self.name+'-'+self.email+'-'+self.nation


class datepicker(models.Model):
    date =models.CharField(max_length=20)
    def __str__(self):
        return str(self.date)

