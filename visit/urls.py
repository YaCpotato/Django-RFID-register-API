from rest_framework import routers
from .views import VisitViewSet

router = routers.DefaultRouter()
router.register('visits', VisitViewSet)