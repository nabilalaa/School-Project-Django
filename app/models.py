from django.db import models


class Result(models.Model):
    number = models.CharField(null=True, max_length=8)
    name = models.CharField(max_length=50, null=True)
    arabic = models.IntegerField(null=True)
    math = models.IntegerField(null=True)
    science = models.IntegerField(null=True)
    art = models.IntegerField(null=True)

    def __str__(self):
        return self.name
