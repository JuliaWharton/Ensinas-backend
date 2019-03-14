from django.db import models

# Create your models here.
class Materia(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField()
    senha = models.CharField(max_length=256)

    def __str(self):
        return self.email

class Professor(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField()
    senha = models.CharField(max_length=256)
    aprovado = models.BooleanField(default=False)
    materia = models.ForeignKey(Materia, on_delete=models.SET_DEFAULT, default=None)
    curso = models.CharField(max_length=256, default=None)
    instiuicao = models.CharField(max_length=256, default=None)
    alunos = models.ManyToManyField(Aluno, through='Contato')

    def __str(self):
        return self.email

class Contato(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    oculto = models.BooleanField(default=False)