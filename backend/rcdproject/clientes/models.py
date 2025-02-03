from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=300)
    contacto = models.CharField(max_length=50)
    nombre_contacto = models.CharField(max_length=50)
    fecha_ingreso = models.DateField()
    razon_social = models.CharField(max_length=300)
    direccion_fiscal = models.CharField(max_length=300)
    rut = models.CharField(max_length=300)
    mail = models.EmailField(unique=True)
    cronograma = models.TextField()


class SolicitudCliente(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='solicitud', primary_key=True) # revisar id (si puede ser el de cliente mejor)

    #vincular con obra y retiro
