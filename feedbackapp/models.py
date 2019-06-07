from django.db import models

class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateField(max_length=50)
    feedback=models.TextField(max_length=500)