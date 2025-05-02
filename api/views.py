from rest_framework import generics

from feedback.models import FeedBackModel

from .serializers import FeedBackSerializer


class FeedBackCreateAPIView(generics.ListCreateAPIView):
    queryset = FeedBackModel.objects.all()
    serializer_class = FeedBackSerializer
