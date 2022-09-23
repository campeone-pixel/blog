from django.db import models
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

class Base(models.Model):
  id = models.AutoField(primary_key=True)
  fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)
  fecha_modificacion = models.DateField(auto_now=True, auto_now_add=False)
  fecha_eliminacion = models.DateField(auto_now=True, auto_now_add=False)

  class Meta:
    abstract = True

class Category(Base):
  nombre = models.CharField(max_length=100, unique=True)

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

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
  categoria = models.ForeignKey(Category,on_delete=models.CASCADE)
  facebook = models.URLField(null=True, blank=True)
  twitter = models.URLField(null=True, blank=True)
  instagram = models.URLField(null=True, blank=True)

  class Meta:
    verbose_name = 'escritor'
    verbose_name_plural = 'escritores'

  def __str__(self):
    return self.nombre + " " + self.apellido


class Post(Base):
  titulo = models.CharField(max_length=50,unique=True)
  subtitulo = models.CharField(max_length=50,unique=True,null=True,blank=True)
  slug = models.SlugField()
  content = RichTextField()
  imagen_post = models.ImageField(upload_to='images/')
  publicar = models.BooleanField(default=False)
  fecha_creacion = models.DateField(auto_now=True)
  escritor =models.ForeignKey(Escritor,on_delete=models.CASCADE)
  categoria = models.ForeignKey(Category,on_delete=models.CASCADE)
  tag = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
  me_gusta = models.ManyToManyField(User,related_name='blogpost_me_gusta')

  def __str__(self):
    return self.titulo

  def get_absolute_url(self):
    return reverse('blogpost-detail', kwargs={'pk': self.pk})

  @property
  def num_de_comentarios(self):
    return Comment.objects.filter(post=self).count()

  def num_me_gusta(self):
      return self.me_gusta.count()

class Comment(Base):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  autor = models.ForeignKey(User, on_delete=models.CASCADE)
  content = RichTextField()
  

  def __str__(self):
    return str(self.autor) + ', ' + self.post.titulo[:40]
