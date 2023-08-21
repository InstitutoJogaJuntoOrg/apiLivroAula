from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nome")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Gender(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")
    squad = models.CharField(max_length=30, verbose_name="Squad", default="Joga Junto" )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Genero"
        unique_together = (('name', 'squad'))

class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome do livro")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descrição do livro")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Livro"