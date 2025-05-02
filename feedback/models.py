from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class ValidateFileSize:
    def __init__(self):
        self.__limit = 10 * 2**20  # 10Мб

    def __call__(self, value):
        if value.size > self.__limit:
            raise ValidationError(
                f"Максимальный размер файла: {self.__limit / 2 ** 20} МБ"
            )


class FeedBackModel(models.Model):
    FEEDBACK_TYPE_CHOICES = [
        ("suggestion", "Пожелание"),
        ("problem", "Проблема"),
        ("complaint", "Претензия"),
        ("other", "Другое"),
    ]
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPE_CHOICES)
    description = models.TextField()
    attachment = models.FileField(
        upload_to="attachments/", null=True, blank=True, validators=[ValidateFileSize()]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.feedback_type} - {self.description[:20]}"
