from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from measurements import api_view


router1 = DefaultRouter()
router1.register("", api_view.ProjectApiView)

router2 = DefaultRouter()
router2.register("", api_view.MeasurementApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/place/", include(router1.urls)),
    path("api/v1/temperature/", include(router2.urls))
]

