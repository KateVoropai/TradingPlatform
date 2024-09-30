from rest_framework import routers

from inventory.views import InventoryViewSet

router = routers.SimpleRouter()
router.register("inventory", InventoryViewSet)

urlpatterns = router.urls
