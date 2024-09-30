from rest_framework import routers

from price.views import PriceViewSet

router = routers.SimpleRouter()
router.register("price", PriceViewSet)

urlpatterns = router.urls
