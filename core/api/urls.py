from django.urls import path
from .views import PostApiListView,PostDetailApiView
app_name = 'api'
urlpatterns = [
    path('',PostApiListView.as_view(),name='list'),
    path('<int:pk>',PostDetailApiView.as_view(),name='detail'),
]