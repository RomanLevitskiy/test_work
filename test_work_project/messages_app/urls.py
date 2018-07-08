from rest_framework.routers import SimpleRouter

from .views import SubscriberViewSet
from simple_history.models import HistoricalRecords

router = SimpleRouter()
router.register("messages", SubscriberViewSet)
router.register("messages/([0-9]+)/history", SubscriberViewSet) 
#router.register("messages/([0-9]+)/history", SubscriberViewSet.id_history()) 
#router.register("messages/([0-9]+)/history", SubscriberViewSet.id_history(1)) 

urlpatterns = router.urls

#urlpatterns.append(url(r'^login', login))
