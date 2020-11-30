from rest_framework import serializers
from clinica.models import Category

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MedicoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "usuario_actualizar", "desc_servicio", "medico")
