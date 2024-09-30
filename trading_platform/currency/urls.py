from rest_framework import routers

from currency.views import CurrencyViewSet

router = routers.SimpleRouter()
router.register("currency", CurrencyViewSet)

urlpatterns = router.urls
