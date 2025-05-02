from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from .models import FeedBackModel

# Create your views here.


def index(request):
    if request.method == "POST":
        feedback_type = request.POST.get("type")
        description = request.POST.get("description")
        attachment = request.FILES.get("attachment")

        if not feedback_type or not description:
            messages.error(request, "Заполните обязателные поля")
            return redirect(reverse("home"))
        if attachment and attachment.size > 10 * 2**20:
            messages.error(request, "Размер файла не должен превышать 10МБ")
            return redirect(reverse("home"))

        try:
            FeedBackModel.objects.create(
                feedback_type=feedback_type,
                description=description,
                attachment=attachment,
            )
            messages.success(request, "Обращение успешно отправлено!")
            return redirect(reverse("home"))
        except Exception as e:
            messages.error(request, f"Ошибка: {str(e)}")
            return redirect(reverse("home"))
    return render(request, template_name="feedback/feedback_form.html")
