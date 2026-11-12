from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=128)


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mostrar = models.CharField(max_length=256)


class Materia(models.Model):
    nombre = models.CharField(max_length=128)
    cant_alumnos = models.IntegerField(default=5)
    id_carrera = models.ForeignKey(
        Carrera,
        on_delete=models.PROTECT,
        db_column='id_carrera'
    )
    id_profesor = models.ForeignKey(
        Profesor,
        on_delete=models.PROTECT,
        db_column='id_profesor'
    )


class Aula(models.Model):
    descripcion = models.CharField(max_length=128)
    ubicacion = models.CharField(max_length=128)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)


class ReservaAula(models.Model):
    id_aula = models.ForeignKey(
        Aula,
        on_delete=models.PROTECT,
        db_column='id_aula'
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256)


class HorarioMateria(models.Model):
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.PROTECT,
        db_column='id_materia'
    )
    id_reserva = models.ForeignKey(
        ReservaAula,
        on_delete=models.PROTECT,
        db_column='id_reserva'
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
