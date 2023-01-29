from django.urls import path
from app_profile import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile", views.ProfileView, basename="profile")
urlpatterns = router.urls
