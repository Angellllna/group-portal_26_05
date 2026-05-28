from django.db import models
from django.conf import settings

class ForumTopic(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='forum_topics',
        verbose_name="Автор"
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="суть")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_closed = models.BooleanField(default=False, verbose_name="Закрыта")

    class Meta:
        verbose_name = "Тема форума"
        verbose_name_plural = "Темы форума"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ForumComment(models.Model):
    topic = models.ForeignKey(
        ForumTopic,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Тема"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='forum_comments',
        verbose_name="Автор"
    )
    content = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
        ordering = ['created_at']

    def __str__(self):
        return f"Коментарий от{self.author} до темы {self.topic.title}"