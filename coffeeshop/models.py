from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Out of Stock'), (1, 'In Stock'))
# Create your models here.
class Coffee(models.Model):
    coffee = models.CharField(max_length=200)
    description = models.TextField()
    weight = models.IntegerField()
    price = models.IntegerField()
    team_member = models.ForeignKey(to=User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.coffee
