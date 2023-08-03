from .views import detail_views, create_article
from django.urls import path

urlpatterns = [
    path('<int:pk>', detail_views, name='detail_views'),
    path('create_article/', create_article, name='create_article'),
]
