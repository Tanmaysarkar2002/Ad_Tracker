from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Advertiser, Location, AdCampaign, AdImpression, AdClick, Transaction
from .serializers import (
    AdvertiserSerializer,
    LocationSerializer,
    AdCampaignSerializer,
    AdImpressionSerializer,
    AdClickSerializer,
    TransactionSerializer,
)

class AdvertiserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

    # Override methods for specific functionalities (optional)
    #  - Implement permission checks (e.g., only authenticated users can access)
    #  - Customize filtering based on user roles

class LocationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Location.objects.all()
        return Location.objects.filter(advertiser=user.advertiser)

class AdCampaignViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdCampaign.objects.all()
    serializer_class = AdCampaignSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return AdCampaign.objects.all()
        return AdCampaign.objects.filter(advertiser=user.advertiser)

class AdImpressionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdImpression.objects.all()
    serializer_class = AdImpressionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return AdImpression.objects.all()
        return AdImpression.objects.filter(campaign__advertiser=user.advertiser)

class AdClickViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdClick.objects.all()
    serializer_class = AdClickSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return AdClick.objects.all()
        return AdClick.objects.filter(campaign__advertiser=user.advertiser)

class TransactionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(advertiser=user.advertiser)
