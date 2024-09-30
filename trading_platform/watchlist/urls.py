from rest_framework import routers

from watchlist.views import WatchlistViewSet

router = routers.SimpleRouter()
router.register("watchlist", WatchlistViewSet)

urlpatterns = router.urls
