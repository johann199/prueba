from django.db import models

# Create your models here.


#### Bailarin ######

class Bailarin(models.Models):
    TIPODOCUMENTO = (
        ("CC", "Cédula de ciudadnaia"),
        ("TI", "Tarjeta de identidad"),
        ("PPN", "Pasapoete"),
        ("RC", "Registro Civil"),
    )
    GENERO = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("LGTBIQ+", "LGTBIQ+"),
        ("OT", "Otro"),
    )
    
    nombre = models.CharField(max_length=60, verbose_name="Nombre*")
    apellido = models.CharField(max_length=60, verbose_name="Apellido*")
    nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=200, verbose_name="Lugar de nacimiento*")
    edad = models.CharField(max_length=2, verbose_name="Edad*")
    tipo_documento = models.CharField(choices=TIPODOCUMENTO, verbose_name="Tipo Documento*")
    identificacion = models.CharField(max_length=6, verbose_name="Identificacion*")
    direccion= models.CharField(max_length=60, verbose_name="Dirección*")
    #ciudad = models.CharField(max_length=60, verbose_name="Ciudad*")
    #departamento = models.CharField(max_length=60, verbose_name="departamento*")
    telefono = models.CharField(max_length=7, verbose_name="Telefono*")
    celular = models.CharField(max_length=10, verbose_name="Celular*")
    correo = models.CharField(max_length=100, verbose_name="Correo*")
    actividad = models.CharField(max_length=60, verbose_name="Actividad*")
    genero = models.CharField(choices=GENERO, verbose_name="Genero*")
    
    class Meta: 
        default_permissions = ()
        ordering = ['nombre']
        permissions = (
            ('registrar_bailarin', 'Puede registrar un bailarin'),
            ('consultar_bailarin', 'Puede consultar un bailarin'),
            ('actualizar_bailarin', 'Puede actualizar un bailarin'), 
        )
    
    def __str__(self):
        return self.nombre + ' - ' + self.apellido
    
    @staticmethod
    def obtener_bailarin():
        return Bailarin.objects.all()
    
    
    
    

    
    
    
    
    
    
    
    
    
    
