from django.db import models
from django.conf import settings


class Subject(models.Model):
    """Предмет / напрямок гейм-дев навчання."""

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Назва предмету",
    )
    description = models.TextField(
        blank=True,
        verbose_name="Опис",
    )

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Grade(models.Model):
    """Оцінка учня з конкретного предмету."""

    GRADE_CHOICES = [(i, str(i)) for i in range(1, 13)]  # 1–12 балів

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="grades",
        verbose_name="Учень",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="grades",
        verbose_name="Предмет",
    )
    grade = models.PositiveSmallIntegerField(
        choices=GRADE_CHOICES,
        verbose_name="Оцінка",
    )
    comment = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Коментар",
        help_text="За що виставлена оцінка: проєкт, домашка, гейм-джем тощо",
    )
    date_issued = models.DateField(
        verbose_name="Дата виставлення",
    )
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="issued_grades",
        verbose_name="Виставив",
        help_text="Викладач або модератор гейм-клубу",
    )

    class Meta:
        verbose_name = "Оцінка"
        verbose_name_plural = "Оцінки"
        ordering = ["-date_issued", "student__username"]

    def __str__(self):
        return (
            f"{self.student.get_full_name() or self.student.username} | "
            f"{self.subject} | {self.grade} | {self.date_issued}"
        )
