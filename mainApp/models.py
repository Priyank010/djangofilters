from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    roll_number = models.PositiveIntegerField(default=0)
    marks = models.PositiveIntegerField(default=0)
    exam_passed = models.BooleanField(default=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)