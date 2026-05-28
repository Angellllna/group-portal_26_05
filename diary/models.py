from django.db import models
from django.conf import settings


class TrainingSubject(models.Model):
    """Навчальний предмет / дисципліна курсантів.

    Приклади: Планування операцій, Маскування, Командна робота,
    Аналіз систем безпеки, Стратегія втечі, Шифри та коди.
    """

    title = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Назва предмету",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Опис",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата створення",
    )

    class Meta:
        verbose_name = "Навчальний предмет"
        verbose_name_plural = "Навчальні предмети"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Grade(models.Model):
    """Оцінка курсанта з навчального предмету."""

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grades",
        verbose_name="Курсант",
    )
    subject = models.ForeignKey(
        TrainingSubject,
        on_delete=models.CASCADE,
        related_name="grades",
        verbose_name="Предмет",
    )
    score = models.PositiveSmallIntegerField(
        verbose_name="Оцінка",
    )
    comment = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Коментар",
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="issued_grades",
        verbose_name="Інструктор",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата виставлення",
    )

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.student.username} | {self.subject} | {self.score}"
        )
