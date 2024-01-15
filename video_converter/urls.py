from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

# 1. description
## 2. video se caption
## 3. time cut silnce remover. stable timecutt.
# 4. video pe video merge 
# 5. photo frame by frame overlay

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = [
    path('', include(router.urls)),
]
