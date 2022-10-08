from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(default="default.jpg", upload_to="profile_pics/")
    imagen_pequenia = ImageSpecField(
        source="imagen",
        processors=[ResizeToFill(50, 50)],
        format="JPEG",
        options={"quality": 100},
    )
    imagen_perfil = ImageSpecField(
        source="imagen",
        processors=[ResizeToFill(200, 200)],
        format="JPEG",
        options={"quality": 100},
    )

    def __str__(self):
        return f"{self.usuario.username} Profile"
