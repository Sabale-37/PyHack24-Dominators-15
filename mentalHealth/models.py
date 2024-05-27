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
