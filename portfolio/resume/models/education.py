from django.db import models


class Education(models.Model):
    location = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    cgpa = models.FloatField("CGPA")
    start_date = models.DateField("start date")
    end_date = models.DateField("end date", null=True, blank=True)

    def __str__(self):
        return self.location
