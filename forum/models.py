from django.conf import settings
from django.db import models


class ForumTopic(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_topics",
        verbose_name="Автор",
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Зміст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_closed = models.BooleanField(default=False, verbose_name="Закрита")

    class Meta:
        verbose_name = "Тема форуму"
        verbose_name_plural = "Теми форуму"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ForumComment(models.Model):
    topic = models.ForeignKey(
        ForumTopic,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Тема",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_comments",
        verbose_name="Автор",
    )
    content = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"
        ordering = ["created_at"]

    def __str__(self):
        return f"Коментар від {self.author} до теми «{self.topic.title}»"
