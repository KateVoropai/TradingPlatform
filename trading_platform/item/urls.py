from rest_framework import routers

from item.views import ItemViewSet

router = routers.SimpleRouter()
router.register("item", ItemViewSet)

urlpatterns = router.urls
