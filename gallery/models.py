from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MediaItem(models.Model):
    class MediaType(models.TextChoices):
        PHOTO = "photo", "Фото"
        SCREENSHOT = "screenshot", "Скріншот"
        VIDEO = "video", "Відео"

    class Category(models.TextChoices):
        OPERATION = "operation", "Операція"
        TRAINING = "training", "Тренування"
        EVENT = "event", "Подія"
        OTHER = "other", "Інше"

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="media_items",
        verbose_name="Автор",
    )
    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(blank=True, verbose_name="Опис")
    file = models.FileField(upload_to="gallery/", verbose_name="Файл")
    media_type = models.CharField(
        max_length=20,
        choices=MediaType.choices,
        default=MediaType.PHOTO,
        verbose_name="Тип медіа",
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
        verbose_name="Категорія",
    )
    action_name = models.CharField(max_length=255, verbose_name="Назва події")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    is_approved = models.BooleanField(default=False, verbose_name="Схвалено")

    class Meta:
        verbose_name = "Медіа-матеріал"
        verbose_name_plural = "Медіа-матеріали"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()}) — {self.author}"