from django.db import models

class Professor(models.Model):
  GRADUADO = 'G'
  ESPECIALISTA = 'E'
  MESTRE = 'M'
  DOUTOR = 'D'

  TITULACAO_CHOICES = [
    (GRADUADO, 'Graduado'),
    (ESPECIALISTA, 'Especialista'),
    (MESTRE, 'Mestre'),
    (DOUTOR, 'Doutor'),
  ]
  
  matricula = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=50)
  endereco = models.CharField(max_length=200)
  telefone = models.CharField(max_length=11)
  titulacao = models.CharField(max_length=1, choices= TITULACAO_CHOICES)

  @staticmethod
  def get_choice(name):
    for choice in Professor.TITULACAO_CHOICES:
      code, choice_name = choice
      if choice_name == name:
        return code
    return ""