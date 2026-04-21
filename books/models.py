# importamos el modulo model pra definir los modelos
from django.db import models

# se defini category que representa las categoria de los libros
class Category(models.Model):
    # se creo title para guardar letras
    title = models.CharField(max_length=250)

    # metodo pra visualizar el objeto
    def __str__(self):
        return self.title  # da el titulo de la categoria

# book para los libros
class Book(models.Model):
    # title para el titulo del libro
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)  # author para autor del libro
    image = models.CharField(max_length=2000)  # image para la imagen del libro

    # created_at para la fecha en que se crea el libro
    created_at = models.DateTimeField(auto_now_add=True)
    # Actualizacion del libro
    update_at = models.DateTimeField(auto_now=True)

    # se crea la relacion con Category, ahora opcional
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,   # si borras la categoría, el libro queda con category=None
        null=True,                   # permite valores nulos en la base de datos
        blank=True,                  # permite que el formulario lo deje vacío
        related_name='books'
    )

    # devolver el objeto de forma legible
    def __str__(self):
        return self.title  # da el título del libro como su representación
