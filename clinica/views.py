from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers

from .models import Category, SubCategory
from .forms import FormCreate, FormCreateSubCategory

def wsmedicos(request):
    data = serializers.serialize("json", Category.objects.all())
    return HttpResponse(data, content_type= "application/json")

def wsmedicos2(request):
    data = serializers.serialize("xml", Category.objects.all())
    return HttpResponse(data, content_type= "application/xml")

# Create your views here.

### CREATE ###
class NewCategory(generic.CreateView):
    template_name = "clini/newcategory.html"
    model = Category
    form_class = FormCreate
    success_url = reverse_lazy("clini:list")

### READ ###
class List(generic.ListView):
    template_name = "clini/list.html"
    model = Category

class Detail(generic.DetailView):
    template_name = "clini/detail.html"
    model = Category
### UPDATE ###
class UpdateCategory(generic.UpdateView):
    template_name = "clini/update.html"
    model = Category
    form_class = FormCreate
    success_url = reverse_lazy("clini:list")
### DELETE ###
class DeleteCategory(generic.DeleteView):
    template_name = "clini/delete_category.html"
    model = Category
    form_class = FormCreate
    success_url = reverse_lazy("clini:list")



### Sub category CRUD###


### READ ###
class ListSubCategory(generic.ListView):
    template_name = "clini/list_subcategory.html"
    queryset = SubCategory.objects.all().order_by('id')

class DetailSubCategory(generic.DetailView):
    template_name = "clini/detail_subcategory.html"
    model = SubCategory

### CREATE ###
class NewSubCategory(generic.CreateView):
    template_name = "clini/new_subcategory.html"
    model = SubCategory
    form_class = FormCreateSubCategory
    success_url = reverse_lazy("clini:list_subcategory")

### UPDATE ###
class UpdateSubCategory(generic.UpdateView):
    template_name = "clini/update_subcategory.html"
    model = SubCategory
    form_class = FormCreateSubCategory
    success_url = reverse_lazy("clini:list_subcategory")

### DELETE ###
class DeleteSubCategory(generic.DeleteView):
    template_name = "clini/delete_subcategory.html"
    model = SubCategory
    form_class = FormCreateSubCategory
    success_url = reverse_lazy("clini:list_subcategory")

def medicoTraumatologia(request):
    context = {
        "medicos": Category.objects.filter(desc_servicio__startswith="Traumatologia")
    }
    return render(request, "clini/trauma.html", context)
