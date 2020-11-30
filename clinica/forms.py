from django import forms

from .models import Category, SubCategory

class FormCreate(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
        "medico",
        "usuario_actualizar",
        "desc_servicio"

        ]

class FormCreateSubCategory(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = [
        "medico",
        "categoria",
        "usuario_actualizar",
        "description"

        ]
