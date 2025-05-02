from django.urls import path

from . import views

urlpatterns = [
    path("v1/feedback", views.FeedBackCreateAPIView.as_view(), name="feedback-api")
]
