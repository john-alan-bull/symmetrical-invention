from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ActivityViewSet, api_root

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
