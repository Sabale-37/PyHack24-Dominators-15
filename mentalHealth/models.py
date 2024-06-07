from django.db import models
from django.contrib.auth.models import User

class LifestyleData(models.Model):
    
    anxiety_level = models.FloatField()
    mental_health_history = models.FloatField()
    depression = models.FloatField()
    headache = models.FloatField()
    sleep_quality = models.FloatField()
    safety = models.FloatField()
    academic_performance = models.FloatField()
    future_career_concerns = models.FloatField()
    social_support = models.FloatField()
    peer_pressure = models.FloatField()
    extracurricular_activities = models.FloatField()
    bullying = models.FloatField()
    prediction = models.CharField(max_length=100)

    def __str__(self):
        return f"LifestyleData({self.pk})"


# models.py
class Sentiment(models.Model):
    positive = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)

    def update_sentiment(self, sentiment):
        if sentiment == 0:
            self.negative += 1
        elif sentiment == 1:
            self.neutral += 1
        elif sentiment == 2:
            self.positive += 1
        self.save()
    
    def total(self):
        return self.positive + self.neutral + self.negative
