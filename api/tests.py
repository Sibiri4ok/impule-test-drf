from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .serializers import FeedBackSerializer


class FeedbackSerializerTest(TestCase):
    def test_valid_data(self):
        data = {"feedback_type": "problem", "description": "Valid data"}
        serializer = FeedBackSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_file_validation(self):
        large_file = SimpleUploadedFile("large.txt", b"x" * (10 * 2**20))
        data = {
            "feedback_type": "problem",
            "description": "Invalid file",
            "attachment": large_file,
        }
        serializer = FeedBackSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_file_validation_error(self):
        large_file = SimpleUploadedFile("large.txt", b"x" * (10 * 2**20 + 1))
        data = {
            "feedback_type": "problem",
            "description": "Invalid file",
            "attachment": large_file,
        }
        serializer = FeedBackSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("attachment", serializer.errors)
