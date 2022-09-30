from email.policy import default
from xmlrpc.client import boolean
from django.db import models
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    estado=models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Category(Base):
    slug = models.SlugField(null=True, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    imagen_categoria = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class Tag(Base):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    descripcion = RichTextField()

    def __str__(self):
        return self.nombre


class Escritor(Base):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Category,  on_delete=models.CASCADE)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "escritor"
        verbose_name_plural = "escritores"

    def __str__(self):
        return self.nombre + " " + self.apellido


class Post(Base):
    titulo = models.CharField(max_length=300, unique=True)
    subtitulo = models.CharField(max_length=300, unique=True, null=True, blank=True)
    slug = models.SlugField()
    content = RichTextField()
    imagen_post = models.ImageField(upload_to="images/",null=True, blank=True)
    publicar = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now=True)
    escritor = models.ForeignKey(Escritor, related_name='posts',on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts")
    tag = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
  

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('ver_articulo',args=[self.slug])
    
    @property
    def num_de_comentarios(self):
        return Comment.objects.filter(post=self).count()

class Comment(Base):
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE,null=True,blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    contenido = models.TextField()
    

    def __str__(self):
        return str(self.contenido) 

    class Meta:
        ordering = ('fecha_creacion',)
    


