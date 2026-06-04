from django.conf import settings
from django.db import models


class Profile(models.Model):

    class Role(models.TextChoices):
        CADET = "cadet", "Cadet"
        INSTRUCTOR = "instructor", "Instructor"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="User",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CADET,
        verbose_name="Role",
    )
    codename = models.CharField(
        max_length=64,
        unique=True,
        verbose_name="Codename",
        help_text="Unique operative alias (e.g. Ghost, Cipher, Nova)",
    )
    bio = models.TextField(
        blank=True,
        default="",
        verbose_name="Bio",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.codename} ({self.get_role_display()})"
