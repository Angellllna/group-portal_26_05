from django.db import models
from django.conf import settings

class Announcement(models.Model):
    PRIORITY_CHOICES = [
        ('normal', 'Normal'),
        ('important', 'Important'),
        ('urgent', 'Urgent'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст оголошення")
    
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='normal',
        verbose_name="Пріоритет"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оновлення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

class Meta:
    verbose_name = "Оголошення"
    verbose_name_plural = "Оголошення"
    ordering = ['-created_at']

    def __str__(self):
        return self.title