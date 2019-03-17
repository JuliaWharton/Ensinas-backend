from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Matéria"
        verbose_name_plural = "Matérias"

class Estudante(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(verbose_name="E-mail")
    senha = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.nome} ({self.email})'

class Mentor(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(verbose_name="E-mail")
    senha = models.CharField(max_length=256)
    aprovado = models.BooleanField(default=False)
    materia = models.ForeignKey(Materia, on_delete=models.SET_DEFAULT, default=None, verbose_name="Matéria")
    curso = models.CharField(max_length=256, default=None)
    instituicao = models.CharField(max_length=256, default=None, verbose_name="Instituição")
    estudantes = models.ManyToManyField(Estudante, through='Solicitacao')

    def __str__(self):
        return f'{self.nome} ({self.email})'

    class Meta:
        verbose_name_plural = "Mentores"

class Solicitacao(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    oculto = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.estudante} - {self.mentor}'

    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"