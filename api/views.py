from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .serializers import MedicoSerializer, MedicoDetailSerializer
from rest_framework.response import Response

from clinica.models import Category

class MedicoList(APIView):
    def get(self, request):
        medicos = Category.objects.all()
        data = MedicoSerializer(medicos, many=True).data
        return Response(data)

class MedicoDetail(APIView):
    def get(self, request, pk):
        medico = get_object_or_404(Category, pk=pk)
        data = MedicoDetailSerializer(medico).data
        return Response(data)
