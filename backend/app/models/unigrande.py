from tortoise import fields, models
from datetime import datetime

class PeriodoLetivo(models.Model):
    id: int = fields.IntField(pk=True)
    ano: int = fields.IntField()
    semestre: int = fields.IntField()
    data_inicio: datetime = fields.DatetimeField()
    data_fim: datetime = fields.DatetimeField()

    class Meta:
        table = "periodo_letivo"
        unique_together = (("ano", "semestre"),)

class Professor(models.Model):
    pass

class Curso(models.Model):
    pass

class Disciplina(models.Model):
    pass

class Matriz(models.Model):
    pass

class Turma(models.Model):
    pass

class Aluno(models.Model):
    pass