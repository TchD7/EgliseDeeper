from django.shortcuts import render
from .forms import EnfantsPostForm
from .models import EnfantsPost
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Eglises.models import Districts, Groups
from Supports.models import Sexe, Region
from django.core.paginator import Paginator
from JeunesApps.resources import EnfantsPostResource
from django.http import HttpResponse




def export_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        jeunes_resource = EnfantsPostResource()
        dataset = jeunes_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'export.html')




class AddEnfants(CreateView):
    model = EnfantsPost
    form_class = EnfantsPostForm
    template_name = 'add_enfant.html' 

class EnfantList(ListView):
    model = EnfantsPost
    template_name = 'enfants_list.html'
    paginate_by = 20
    
    def get_context_data(self, *args, **kwargs):
        District_list = Districts.objects.all()
        Groupe_list = Groups.objects.all()
        Region_list = Region.objects.all()
        Sexe_list = Sexe.objects.all()
        Enfants_nombre = EnfantsPost.objects.all().count()
        context = super(EnfantList, self).get_context_data(*args, **kwargs)
        context["District_list"] = District_list
        context["Groupe_list"] = Groupe_list
        context["Region_list"] = Region_list
        context["Sexe_list"] = Sexe_list
        context["Enfants_nombre"] = Enfants_nombre
        return context


def EnfantTableList(request):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Enfant_Table_list = EnfantsPost.objects.all()
    Enfant_Table_list_count = EnfantsPost.objects.all().count()
    return render(request, 'enfants_table_list.html', {'Enfant_Table_list':Enfant_Table_list, 'Enfant_Table_list_count':Enfant_Table_list_count, 'District_list':District_list, 'Groupe_list':Groupe_list, 'Region_list':Region_list})     


def EnfantsDetail(request, id):
    Enfants_detail = EnfantsPost.objects.filter(pk=id)
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    return render(request, 'enfants_detail.html', {'Enfants_detail':Enfants_detail, 'Groupe_list':Groupe_list, 'Region_list':Region_list})

class EditeEnfants(UpdateView):
    model = EnfantsPost
    form_class = EnfantsPostForm
    template_name = 'edite_enfant.html'
    
class DeleteEnfants(DeleteView):
    model = EnfantsPost
    form_class = EnfantsPostForm
    template_name = 'delete_enfant.html' 
    success_url = reverse_lazy('enfants_list')



def Search_Enfants(request):
    if request.method == 'POST':
        enfant_search = request.POST['enfant_search']
        Enfants_nom = EnfantsPost.objects.filter(nom__contains=enfant_search)
        Enfants_nom_count = EnfantsPost.objects.filter(nom__contains=enfant_search).count()
        Groupe_list = Groups.objects.all()
        return render(request, 'search_enfants.html', {'enfant_search':enfant_search, 'Enfants_nom':Enfants_nom, 'Enfants_nom_count':Enfants_nom_count, 'Groupe_list':Groupe_list})
    else:
        return render(request, 'search_enfants.html', )

def FilterEnfantsDistrict(request, dist):
    District_list = Districts.objects.all()
    Enfants_district = EnfantsPost.objects.filter(district=dist) 
    Enfants_district_count = EnfantsPost.objects.filter(district=dist).count() 
    return render(request, 'enfants_district.html', {'Enfants_district':Enfants_district, 'District_list':District_list, 'dist':dist, 'Enfants_district_count':Enfants_district_count})

def FilterEnfantsGroupe(request, group):
    Groupe_list = Groups.objects.all()
    Enfants_groupe = EnfantsPost.objects.filter(groupe=group)
    Enfants_groupe_count = EnfantsPost.objects.filter(groupe=group).count()  
    return render(request, 'enfants_groupe.html', {'Enfants_groupe':Enfants_groupe, 'Groupe_list':Groupe_list, 'group':group, 'Enfants_groupe_count':Enfants_groupe_count})

def FilterEnfantsRegion(request, regs):
    Region_list = Region.objects.all()
    Enfants_region = EnfantsPost.objects.filter(region=regs)
    Enfants_region_count = EnfantsPost.objects.filter(region=regs).count()  
    return render(request, 'enfants_region.html', {'Enfants_region':Enfants_region, 'regs':regs, 'Region_list':Region_list, 'Enfants_region_count':Enfants_region_count})

def FilterEnfantsSexe(request, sexs):
    Sexe_list = Sexe.objects.all()
    Enfants_sexe = EnfantsPost.objects.filter(sexe=sexs)
    Enfants_sexe_count = EnfantsPost.objects.filter(sexe=sexs).count()  
    return render(request, 'enfants_sexe.html', {'Enfants_sexe':Enfants_sexe, 'Sexe_list':Sexe_list, 'sexs':sexs, 'Enfants_sexe_count':Enfants_sexe_count})

      
def FilterEnfantsDistrictTable(request, dist):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Enfants_district_table = EnfantsPost.objects.filter(district=dist) 
    Enfants_district_count_table = EnfantsPost.objects.filter(district=dist).count() 
    return render(request, 'enfants_district_table.html', {'Enfants_district_table':Enfants_district_table, 'District_list':District_list, 'dist':dist, 'Enfants_district_count_table':Enfants_district_count_table, 'Groupe_list':Groupe_list, 'Region_list':Region_list})

def FilterEnfantsGroupeTable(request, group):
    District_list = Districts.objects.all()
    Groupe_list = Groups.objects.all()
    Region_list = Region.objects.all()
    Enfants_groupe_table = EnfantsPost.objects.filter(groupe=group)
    Enfants_groupe_count_table = EnfantsPost.objects.filter(groupe=group).count()  
    return render(request, 'enfants_groupe_table.html', {'Enfants_groupe_table':Enfants_groupe_table, 'Groupe_list':Groupe_list, 'group':group, 'Enfants_groupe_count_table':Enfants_groupe_count_table, 'District_list':District_list, 'Region_list':Region_list})








