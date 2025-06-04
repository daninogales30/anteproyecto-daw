from django.db import models


class Entrada(models.Model):
    title = models.CharField("Título", max_length=200)
    body = models.TextField("Contenido")
    user = models.ForeignKey(
        'persons.Person',
        on_delete=models.CASCADE,
        related_name='user_entry',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
