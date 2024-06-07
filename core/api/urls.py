from django.urls import path
from .views import PostApiListView,PostDetailApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'api'
urlpatterns = [
    path('',PostApiListView.as_view(),name='list'),
    path('<int:pk>',PostDetailApiView.as_view(),name='detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]