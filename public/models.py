from django.db import models

# Create your models here.

class Omov_alumno(models.Model):
	cve_alumno 				= models.CharField(primary_key=True, max_length=9)
	cve_ciclo 				= models.PositiveSmallIntegerField()
	cve_estatus 			= models.PositiveSmallIntegerField()
	cve_carrera 			= models.CharField(max_length=8)
	cve_escuela 			= models.CharField(max_length=8)
	semestre 				= models.PositiveSmallIntegerField()
	cve_plan 				= models.CharField(max_length=5)
	no_incluir 				= models.CharField(max_length=1)
	fecha_mov 				= models.DateTimeField()
	registro				= models.IntegerField()
	alumno_id				= models.IntegerField()
	mov_alumno_id			= models.IntegerField()
	carrera_id				= models.IntegerField()
	ciclo_id				= models.IntegerField()
	escuela_id				= models.IntegerField()
	plan_estudio_id			= models.IntegerField()
	estatus_id				= models.IntegerField()
	f_reg 					= models.DateTimeField()
	mod_tit_id				= models.IntegerField()
	veredicto_examen_id		= models.IntegerField()

	class Meta:
		managed 	= False
		db_table 	= '"DESARROLLO"."MOV_ALUMNO"'
		app_label 	= 'desarrollo'