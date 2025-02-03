from rest_framework import serializers
from .models import Cliente, SolicitudCliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [ 'id', 'nombre', 'direccion', 'contacto', 'nombre_contacto', 'fecha_ingreso', 'razon_social', 'direccion_fiscal', 'rut', 'mail', 'cronograma' ]
        read_only_fields = ['id']

class SolicitudClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudCliente
        fields = [
            'estado', 'fecha_solicitud' ]
        read_only_fields = ['id', 'fecha_solicitud', 'estado']

class SolicitudClienteAdminSerializer(serializers.ModelSerializer):
    """
    Serializador para el administrador, que permite actualizar el estado.
    """
    class Meta:
        model = SolicitudCliente
        fields = [
            'estado', 'fecha_solicitud'
        ]
        read_only_fields = ['id', 'fecha_solicitud']
