from django.db import models

# Create your models here.
class Book(models.Model):
    objects = None
    title = models.CharField(max_length=50)
    price = models.IntegerField(50)

    def __str__(self):
        return '{}'.format(self.title)

    @classmethod
    def get(cls, id):
        pass