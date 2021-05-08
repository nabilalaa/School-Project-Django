from django.db import models


class Result(models.Model):
    number = models.CharField(null=True, max_length=8)
    name = models.CharField(max_length=50, null=True)
    arabic = models.DecimalField(null=True ,max_digits=5,decimal_places=2)
    english = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    math = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    science = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    art = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    belief = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    computer = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    sum = models.DecimalField(null=True,max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name
