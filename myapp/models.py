<<<<<<< HEAD
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):                 # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    lc_classification = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return "%s" % self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

=======
from __future__ import unicode_literals

from django.db import models

# Create your models here.
>>>>>>> 47e9abd8d7de15ddd040ba0b45410a37684185af
