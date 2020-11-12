from rest_framework import routers
from .views import UserViewSet, ProductViewSet, CouponViewSet, CartViewSet, CheckoutViewSet, WishlistViewSet

router = routers.SimpleRouter()

router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)
router.register(r"coupons", CouponViewSet)
router.register(r"carts", CartViewSet)
router.register(r"checkouts", CheckoutViewSet)
router.register(r"wishlists", WishlistViewSet)

urlpatterns = router.urls
