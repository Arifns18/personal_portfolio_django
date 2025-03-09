from django.db import models


class Experience(models.Model):
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    ongoing = models.BooleanField(default=True)
    start_date = models.DateField("start date")
    end_date = models.DateField("end date", null=True, blank=True)

    def __str__(self):
        return self.position
