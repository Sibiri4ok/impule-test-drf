import os

from django.contrib.messages import get_messages
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from django.test import TestCase

from .models import FeedBackModel

# Create your tests here.


class FeedBackModelTest(TestCase):
    def setUp(self):
        self.valid_file = SimpleUploadedFile(
            "test.txt", b"file content", content_type="text/plain"
        )
        self.large_file = SimpleUploadedFile(
            "large.txt", b"x" * (10 * 2**20 + 1), content_type="text/plain"
        )

    def test_create_feedback_without_file(self):
        feedback = FeedBackModel.objects.create(
            feedback_type="problem", description="Test description"
        )
        self.assertEqual(feedback.feedback_type, "problem")
        self.assertFalse(feedback.attachment)

    def test_create_feedback_with_file(self):
        feedback = FeedBackModel.objects.create(
            feedback_type="suggestion",
            description="Test with file",
            attachment=self.valid_file,
        )
        self.assertTrue(os.path.exists(feedback.attachment.path))

    def test_file_size_validation_error(self):
        feedback = FeedBackModel.objects.create(
            feedback_type="problem",
            description="Large file",
            attachment=self.large_file,
        )
        with self.assertRaises(ValidationError):
            feedback.full_clean()


class FeedbackViewTest(TestCase):
    def test_valid_submission(self):
        data = {"type": "problem", "description": "Описание"}
        response = self.client.post(reverse("home"), data)
        self.assertRedirects(response, reverse("home"))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("Обращение успешно отправлено!", str(messages[0]))

    def test_file_size_validation(self):
        large_file = SimpleUploadedFile("large.txt", b"x" * (10 * 2**20 + 1))
        data = {
            "type": "problem",
            "description": "Large file",
            "attachment": large_file,
        }
        response = self.client.post(reverse("home"), data)
        self.assertRedirects(response, reverse("home"))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("Размер файла не должен превышать 10МБ", str(messages[0]))
