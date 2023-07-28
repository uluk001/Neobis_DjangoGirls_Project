from .views import detail_views
from django.urls import path

urlpatterns = [
    path('<int:pk>', detail_views, name='detail_views'), 
]
