from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente, SolicitudCliente
from .serializers import (
    ClienteSerializer,
    SolicitudClienteSerializer,
    SolicitudClienteAdminSerializer
)

class RegistroCliente(APIView):
    """
    Endpoint para que un cliente se registre.
    Crea un registro en Cliente y, a la vez, una SolicitudCliente en estado "pendiente".
    """
    def post(self, request):
        serializer_cliente = ClienteSerializer(data=request.data)
        if serializer_cliente.is_valid():
            cliente = serializer_cliente.save()
            # Se crea la solicitud con estado por defecto "pendiente"
            solicitud = SolicitudCliente.objects.create(cliente=cliente)
            return Response({
                'mensaje': 'Cliente registrado, pendiente de aprobación.',
                'cliente': ClienteSerializer(cliente).data,
                'solicitud': SolicitudClienteSerializer(solicitud).data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer_cliente.errors, status=status.HTTP_400_BAD_REQUEST)

class ListarSolicitudesCliente(APIView):
    """
    Lista todas las solicitudes de alta de cliente (para el administrador).
    """
    def get(self, request):
        solicitudes = SolicitudCliente.objects.all()
        serializer = SolicitudClienteAdminSerializer(solicitudes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AprobarSolicitudCliente(APIView):
    """
    Permite al administrador aprobar una solicitud.
    """
    def put(self, request, pk):
        try:
            solicitud = SolicitudCliente.objects.get(pk=pk)
        except SolicitudCliente.DoesNotExist:
            return Response({'error': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        if solicitud.estado != 'pendiente':
            return Response({'error': 'La solicitud ya ha sido procesada.'}, status=status.HTTP_400_BAD_REQUEST)
        
        solicitud.estado = 'aceptado'
        solicitud.save()
        
        return Response({'mensaje': 'Solicitud aprobada.'}, status=status.HTTP_200_OK)

class RechazarSolicitudCliente(APIView):
    """
    Permite al administrador rechazar una solicitud.
    """
    def put(self, request, pk):
        try:
            solicitud = SolicitudCliente.objects.get(pk=pk)
        except SolicitudCliente.DoesNotExist:
            return Response({'error': 'Solicitud no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        if solicitud.estado != 'pendiente':
            return Response({'error': 'La solicitud ya ha sido procesada.'}, status=status.HTTP_400_BAD_REQUEST)
        
        solicitud.estado = 'rechazado'
        solicitud.save()
        
        return Response({'mensaje': 'Solicitud rechazada.'}, status=status.HTTP_200_OK)
