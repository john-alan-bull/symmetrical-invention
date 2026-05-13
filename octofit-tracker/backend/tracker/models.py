from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
