from django.contrib.auth.models import User
from django.db import models


class Advertiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Location(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)  
    longitude = models.DecimalField(max_digits=10, decimal_places=6)  
    address = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        if self.address:
            return f"{self.address}"
        else:
            return f"({self.latitude}, {self.longitude})"


class AdCampaign(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    cost_per_impression = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cost_per_click = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calculate_spend(self):
        total_spend = 0
        if self.cost_per_impression:
            impressions = AdImpression.objects.filter(campaign=self).aggregate(total_count=Sum('count'))['total_count'] or 0
            total_spend += impressions * self.cost_per_impression
        if self.cost_per_click:
            clicks = AdClick.objects.filter(campaign=self).aggregate(total_count=Sum('count'))['total_count'] or 0
            total_spend += clicks * self.cost_per_click
        return total_spend
    
class AdImpression(models.Model):
    campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    count = models.PositiveIntegerField() 

class AdClick(models.Model):
    campaign = models.ForeignKey(AdCampaign, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    count = models.PositiveIntegerField() 




class Transaction(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')])


