from django.db import models

class Escuelas(models.Model):
    cve_escuela = models.CharField(primary_key=True, max_length=10)
    desc_completo = models.CharField(max_length=100)
    desc_corto = models.CharField()
    ubicacion = models.CharField(max_length=30)

    class Meta:
	    managed 	= False
	    db_table 	= 'ESCUELA'
	    app_label 	= 'desarrollo'

class Carreras(models.Model):
    cve_carrera = models.CharField(primary_key=True, max_length=8)
    desc_carrera = models.CharField(max_length=60)
    activa = models.CharField(max_length=10)
    cve_escuela = models.ForeignKey(Escuelas, on_delete=models.CASCADE, null=True, db_column='CVE_ESCUELA')

    class Meta:
	    managed 	= False
	    db_table 	= 'CARRERA'
	    app_label 	= 'desarrollo'

class Plan_estudio(models.Model):
    cve_plan			= models.CharField(primary_key=True ,max_length=5)
    cve_carrera			= models.CharField(max_length=8)
    cve_ciclo			= models.IntegerField()
    cve_ciclo_ini		= models.IntegerField()
    cve_escuela			= models.CharField(max_length=8)
    desc_plan			= models.CharField(max_length=40)
    escuela_id			= models.IntegerField()
    estatus				= models.CharField(max_length=1)
    plan_estudio_id		= models.IntegerField()
    semiescolarizado	= models.CharField(max_length=1)
    tipo_plan			= models.IntegerField()
    num_ciclos			= models.IntegerField()
    val_cred			= models.CharField(max_length=1)
    tot_creditos = models.IntegerField()
    cal_min = models.IntegerField()
    anio = models.CharField()

    class Meta:
        managed		= False
        db_table	= 'PLAN_ESTUDIO'
        app_label	= 'desarrollo'

class Profesor_grupo(models.Model):
	pl_matricula = models.CharField(max_length=8, null=True)
	pl_llave_grupo = models.CharField(primary_key=True, max_length=9, null=True)
	nom = models.CharField(max_length=122)
	f_nacimiento = models.DateField()
	autorizacion = models.CharField(max_length=22)
	pl_ciclo = models.IntegerField(null=True)
	escuela = models.CharField(max_length=8, null=True)

	class Meta:
		managed 	= False
		db_table 	= '"DESARROLLO"."V_PERSONAL_INDICADORES"'
		app_label 	= 'desarrollo'

class Oparametros_dtd(models.Model):
	id	= models.IntegerField(primary_key=True)
	descripcion 	= models.CharField(max_length=4000)
	valor			= models.CharField(max_length=4000)
	fecha_ini		= models.DateField(default='')
	fecha_fin		= models.DateField(default='')

	class Meta:
		managed 	= False
		db_table 	= '"API_ESCOLAR"."PARAMETROS_DTD"'
		app_label 	= 'desarrollo'

class Materias(models.Model):
    materia_id 				= models.CharField(primary_key=True, max_length=5)
    desc_materia 			= models.CharField(null=False, max_length=100)
    cve_materia 			= models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = "MATERIA"
        app_label = 'desarrollo'
        verbose_name_plural = "Materias"

class Ciclo_carrera(models.Model):
	cve_ciclo 				= models.PositiveSmallIntegerField(primary_key=True)
	cve_carrera 			= models.CharField(max_length=8)
	estatus_ciclo 			= models.CharField(max_length=1)
	cve_escuela 			= models.CharField(max_length=8)
	cve_plan 				= models.CharField(max_length=3)
	cve_ciclo_sig			= models.PositiveSmallIntegerField()
	fecha_carta				= models.DateField()

	class Meta:
		managed 	= False
		db_table 	= 'CICLO_CARRERA'
		app_label 	= 'desarrollo'

class Plan_materia(models.Model):
    plan_materia_id 		= models.AutoField(primary_key=True)
    cve_plan       			= models.CharField(max_length=8)
    cve_materia 			= models.CharField(max_length=8)
    horas_semana 			= models.PositiveSmallIntegerField()
    creditos 				= models.PositiveSmallIntegerField()
    semestre 				= models.IntegerField(null=True)
    es_tronco_comun 		= models.BooleanField(default=False)
    es_electiva 			= models.BooleanField(default=False)

    class Meta:
        managed 	= False
        db_table 	= 'PLAN_MATERIA'
        app_label 	= 'desarrollo'