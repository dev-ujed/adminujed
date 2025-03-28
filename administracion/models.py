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