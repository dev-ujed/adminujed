from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
  
class CustomUserManager(BaseUserManager):
    def create_user(self, matricula, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(matricula=matricula, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(matricula, email, password, **extra_fields)

# Modelo personalizado de usuario
class CustomUser(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        db_table = 'custom_user'
    
    # Definir el manager para este modelo
    objects = CustomUserManager()

    # Campos obligatorios para el login y autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['matricula', 'name', 'last_name']

    def __str__(self):
        return self.email

