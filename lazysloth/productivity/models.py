from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TimeTracking(models.Model):
    date = models.DateField(auto_now_add=True)
    work_time = models.DurationField(default=0)  # Duration spent working
    break_time = models.DurationField(default=0)  # Duration spent on breaks

    def __str__(self):
        return f"{self.date}: Work {self.work_time}, Break {self.break_time}"
