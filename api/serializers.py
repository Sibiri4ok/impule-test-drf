from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from feedback.models import FeedBackModel


class FileValidator:
    def __init__(self):
        self.__limit = 10 * 2**20

    def __call__(self, value):
        if value.size > self.__limit:
            raise ValidationError(
                f"Максимальный размер файла: {self.__limit / 2 ** 20} МБ"
            )


class FeedBackSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(
        required=False, allow_null=True, validators=[FileValidator()]
    )

    class Meta:
        model = FeedBackModel
        fields = "__all__"
        extra_kwargs = {"description": {"required": True}, "type": {"required": True}}
