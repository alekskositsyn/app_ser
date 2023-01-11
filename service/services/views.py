from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription
from services.serializers import SubscriptionSerializer


class SubscriptionsView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
