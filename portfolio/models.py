from django.conf import settings
from django.db import models


class Portfolio(models.Model):
    SPECIALIZATIONS = [
        ("planner", "Планувальник"),
        ("hacker", "Хакер"),
        ("master_of_disguise", "Майстер маскування"),
        ("driver", "Водій"),
        ("negotiator", "Переговорник"),
        ("analyst", "Аналітик"),
        ("gunsmith", "Зброяр"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolio",
        verbose_name="Користувач",
    )
    codename = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="Кодове ім'я",
    )
    specialization = models.CharField(
        max_length=32,
        choices=SPECIALIZATIONS,
        default="gunsmith",
        verbose_name="Спеціалізація",
    )
    level = models.PositiveIntegerField(
        default=1,
        verbose_name="Рівень",
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Біографія",
    )
    skills = models.TextField(
        blank=True,
        verbose_name="Навички",
    )
    achievements = models.TextField(
        blank=True,
        verbose_name="Досягнення",
    )
    avatar = models.FileField(
        upload_to="portfolio/",
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Створено",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Оновлено",
    )

    class Meta:
        verbose_name = "Досьє"
        ordering = ["-level", "codename"]

    def __str__(self):
        return f"{self.codename} ({self.user.username}) — {self.get_specialization_display()}"
