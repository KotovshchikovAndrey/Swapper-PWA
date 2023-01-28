from django.urls import path
from app_profile import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("test", views.TestView, basename="user")
urlpatterns = router.urls
