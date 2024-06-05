from rest_framework import serializers
from .models import Advertiser, Location, AdCampaign, AdImpression, AdClick, Transaction

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = '__all__'  # Include all fields for Advertiser model

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'  # Include all fields for Location model

class AdCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCampaign
        fields = '__all__'  # Include all fields for AdCampaign model

class AdImpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImpression
        fields = '__all__'  # Include all fields for AdImpression model

class AdClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdClick
        fields = '__all__'  # Include all fields for AdClick model

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'  # Include all fields for Transaction model
