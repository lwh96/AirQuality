from rest_framework import routers
from .views import CityViewSet

router = routers.DefaultRouter()
router.register(r'city', CityViewSet, base_name='city')

urlpatterns = router.urls