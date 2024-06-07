from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30, default='amazon')
    start_year = models.CharField(max_length=4, default='2020')  # Set default value
    problem_statement = models.TextField(default='Your problem statement')  # Set default value
    solution = models.TextField(default='Solution for that problem statement')  # Set default value
    market_opportunity = models.TextField(default='Market opportunity for the company')  # Set default value
    team = models.IntegerField(default=10)  # Set default value
    description = models.TextField(default='A description of the company')  # Set default value
    image = models.ImageField(upload_to='company_images/')
    revenue = models.CharField(max_length=255, default='1000000')  # Set default value
    founder = models.CharField(max_length=255, default='John Doe')  # Set default value
    investment_round = models.CharField(max_length=255, default='Series A')  # Set default value
    yearwise_revenue = models.JSONField(default=[
        {"year": "2020", "revenue": "500000"},
        {"year": "2021", "revenue": "50034"},
        {"year": "2022", "revenue": "500000"},
        {"year": "2023", "revenue": "40000"}
    ])  # Set default value
    yearwise_growth = models.JSONField(default=[
        {"year": "2020", "growth": "20%"},
        {"year": "2021", "growth": "5%"},
        {"year": "2022", "growth": "2%"},
        {"year": "2023", "growth": "4%"}
    ])  # Set default value
    digital_marketing = models.JSONField(default=[
        {"youtube": "10%", "instagram": "20%", "website": "35%", "other_source": "30%", "facebook": "5%"}
    ])  # Set default value
    financial_graph = models.JSONField(default=[
        { "year": "2020", "total_sales": "10000", "new_income": "5000" },
    { "year": "2021", "total_sales": "20000", "new_income": "7000" },
    { "year": "2022", "total_sales": "22000", "new_income": "4000" },
    { "year": "2023", "total_sales": "9000", "new_income": "3000" }
    ])



class Message(models.Model):
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.from_user} to {self.to_user}"
