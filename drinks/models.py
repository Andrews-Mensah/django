import uuid
from django.db import models

class Drink(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.name + ' ' + self.description