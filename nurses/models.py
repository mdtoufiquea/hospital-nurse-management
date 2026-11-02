
from django.db import models


class Nurse(models.Model):

    nurse_id = models.CharField(max_length=20, unique=True)

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(max_length=10)

    department = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    experience = models.IntegerField()

    image = models.ImageField(
        upload_to='nurse_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
