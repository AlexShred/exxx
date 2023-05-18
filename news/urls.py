from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [
    path('news/', views.NewsListCreateAPIView.as_view()),
    path('news/<int:pk>', views.NewsRetrieveUpdateDestroyAPIView.as_view()),
    path('news/<int:news_id>/comments', views.NewsCommentListCreateAPIView.as_view()),
    path('news/<int:news_id>/comments/<int:pk>/', views.NewsCommentRetrieveUpdateDestroyAPIView.as_view()),

    path('statuses/', views.StatusListCreateAPIView.as_view()),
    path('statuses/<int:pk>', views.StatusRetrieveUpdateDestroyAPIView.as_view()),

    path('news/<news_id>/<slug>/', views.NewsStatusCreateAPIView.as_view())
]