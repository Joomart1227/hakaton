from rest_framework import routers
# from django.contrib.comments.views import comments

from .views import ProductViewSet, FavoriteViewSet


router = routers.DefaultRouter()
router.register('product', ProductViewSet, 'product')
router.register('favorites', FavoriteViewSet, 'favorite')

urlpatterns = router.urls