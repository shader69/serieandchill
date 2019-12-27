import datetime
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Categorie(models.Model):
    name = models.CharField(max_length=30,
                            null=True)

    def __str__(self):
        return self.name


class Nationalite(models.Model):
    name = models.CharField(max_length=30,
                            null=True)

    def __str__(self):
        return self.name


class Serie(models.Model):
    title = models.CharField(max_length=50,
                             blank=False,
                             null=False,
                             default='(no title)')

    description = models.TextField(blank=True,
                                   null=True,
                                   default=None)

    rate = models.FloatField(blank=False,
                             null=False,
                             default=0,
                             validators=[MinValueValidator(0), MaxValueValidator(5)])

    director = models.CharField(max_length=30,
                                blank=False,
                                null=False,
                                default='...')

    actor = models.CharField(max_length=200,
                             blank=True,
                             null=True,
                             default='...')

    epNumb = models.IntegerField(blank=False,
                                 null=False,
                                 default=1,
                                 validators=[MinValueValidator(1), MaxValueValidator(999)])

    seasonNumb = models.IntegerField(blank=False,
                                     null=False,
                                     default=1,
                                     validators=[MinValueValidator(1), MaxValueValidator(999)])

    release = models.DateField(default='2000-01-01',
                               verbose_name="Date de parution")

    nationalite = models.ForeignKey(Nationalite,
                                    default=None,
                                    null=True,
                                    on_delete=models.SET_NULL)

    categories = models.ManyToManyField(Categorie)

    photo = models.ImageField(blank=True,
                              null=True,
                              upload_to="covers")

    def __str__(self):
        result = self.title
        if self.description is not None:
            result += ' : ' + self.description[:80] + '...(voir la suite)'
        return result

    def yearpublished(self):
        return self.release.strftime('%Y')


class Comment(models.Model):
    serie = models.ForeignKey(Serie,
                              null=True,
                              on_delete=models.SET_NULL,
                              related_name='serie')

    creator = models.ForeignKey(User,
                                null=True,
                                on_delete=models.SET_NULL,
                                related_name='creator')

    content = models.TextField(null=False,
                               default=None)

    rate = models.FloatField(blank=False,
                             null=False,
                             default=0,
                             validators=[MinValueValidator(0), MaxValueValidator(5)])

    postdate = models.DateField(default=datetime.date.today,
                                null=False)

    def __str__(self):
        return self.content
