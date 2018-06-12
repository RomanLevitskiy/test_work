from rest_framework.routers import SimpleRouter

from .views import SubscriberViewSet

router = SimpleRouter()
router.register("messages", SubscriberViewSet)

urlpatterns = router.urls

#urlpatterns.append(url(r'^login', login))
