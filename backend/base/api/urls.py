from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.getRoutes),
    path('meters/', views.getMeter),
    path("meters/update/<int:pk>", views.UpdateMeter, name="update values"),
    path("meters/paid/", views.paidBill, name="Bill update"),
    path("meters/get/", views.getMeterCount, name="get meter count"),
    path("meters/get/<int:pk>", views.getMeterId, name="get values"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
