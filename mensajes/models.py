from datetime import datetime
from enum import auto
from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    id = models.AutoField(primary_key=True)
    estado=models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField(auto_now=True, auto_now_add=False)

class Mensajes(Base):
  enviado_por=  models.ForeignKey(User, related_name='sent_messages',on_delete=models.PROTECT)
  recibido_por=  models.ForeignKey(User, related_name='receiver_messages',on_delete=models.PROTECT)
  cuerpo = models.CharField(max_length=500)


