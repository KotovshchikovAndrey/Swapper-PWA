from rest_framework.routers import DefaultRouter

from app_profile import views

router = DefaultRouter()
router.register("profile", views.ProfileViewSet, basename="profile")
urlpatterns = router.urls
