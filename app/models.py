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
                             validators=[MinValueValidator(0), MaxValueValidator(10)])

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

    release = models.DateField(default='2000-01-01',
                               verbose_name="Date de parution")

    nationalite = models.ForeignKey(Nationalite,
                                    default=None,
                                    null=True,
                                    on_delete=models.SET_NULL)

    categorie = models.ManyToManyField(Categorie)

    photo = models.ImageField(blank=True,
                              null=True,
                              upload_to="covers/doriansmomnudes")

    def __str__(self):
        result = self.title
        if self.description is not None:
            result += ' : ' + self.description[:80] + '...(voir la suite)'
        return result
