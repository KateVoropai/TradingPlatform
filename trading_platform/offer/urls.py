from rest_framework import routers

from offer.views import OfferViewSet

router = routers.SimpleRouter()
router.register("offer", OfferViewSet)

urlpatterns = router.urls
