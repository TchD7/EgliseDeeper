from django.shortcuts import render
from .models import Participants, Etablissements, BillanDeLumiere
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import EtablissementForm, ParticipantFrom, BillanDeLumiereFrom
from django.urls import reverse_lazy
from JeunesApps.resources import BillanDeLumiereResource, ParticipantsResource, EtablissementsResource
from django.http import HttpResponse


class AddParticipants(CreateView):
    model = Participants
    template_name = 'Participant/add_participant.html'
    form_class = ParticipantFrom 


class ParticipantList(ListView): 
    model = Participants
    template_name = 'Participant/participants_list.html'
    
    def get_context_data(self, **kwargs):
        Participant_list = Participants.objects.all()
        Participant_list_count = Participants.objects.all().count()
        context = super().get_context_data(**kwargs)
        context["Participant_list"] = Participant_list
        context["Participant_list_count"] = Participant_list_count
        return context
    
def ParticipantsDetail(request, id):
    Participant_detail = Participants.objects.filter(pk=id)
    return render(request, 'Participant/participants_detail.html', {'Participant_detail':Participant_detail}) 

class EditParticipant(UpdateView):
    model = Participants
    template_name = 'Participant/edit_participants.html' 
    form_class = ParticipantFrom 

class DeleteParticipant(DeleteView):
    model = Participants
    template_name = 'Participant/delete_participants.html' 
    success_url = reverse_lazy('participants_list')
   

def export_participant_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        participant_resource = ParticipantsResource()
        dataset = participant_resource.export()
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

    return render(request, 'Participant/participant_export.html')




class EtsList(ListView): 
    model = Etablissements
    template_name = 'Ecole/Ets_list.html'
    
    def get_context_data(self, *args, **kwargs):
        Etablissements_list = Etablissements.objects.all()
        Etablissements_list_count = Etablissements.objects.all().count()
        context = super(EtsList, self).get_context_data(*args, **kwargs)
        context["Etablissements_list"] = Etablissements_list
        context["Etablissements_list_count"] = Etablissements_list_count
        return context

class AddEtablissement(CreateView):
    model = Etablissements
    template_name = 'Ecole/add_etablisement.html'
    form_class = EtablissementForm 
    
class EditEtablissement(UpdateView):
    model = Etablissements
    template_name = 'Ecole/edit_etablissements.html'
    form_class = EtablissementForm  

class DeleteEtablissement(DeleteView):
    model = Etablissements
    template_name = 'Ecole/delete_etablissements.html' 
    success_url = reverse_lazy('etablissements_list')



def export_ecoles_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        etablissements_resource = EtablissementsResource()
        dataset = etablissements_resource.export()
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

    return render(request, 'Ecole/ecoles_export.html')



class BillanDeLumiereList(ListView):
    model = BillanDeLumiere
    template_name = 'Lumiere/lumieres_list.html'
    
    def get_context_data(self, *args, **kwargs):
        Lumieres_list = BillanDeLumiere.objects.all()
        Lumieres_list_count = BillanDeLumiere.objects.all().count()
        context = super(BillanDeLumiereList, self).get_context_data(*args, **kwargs)
        context["Lumieres_list"] = Lumieres_list
        context["Lumieres_list_count"] = Lumieres_list_count
        return context

class AddBillanDeLumiere(CreateView):
    model = BillanDeLumiere
    template_name = 'Lumiere/add_lumieres.html'
    form_class = BillanDeLumiereFrom 
    
class EditBillanDeLumiere(UpdateView):
    model = BillanDeLumiere
    template_name = 'Lumiere/edit_lumieres.html'
    form_class = BillanDeLumiereFrom  

class DeleteBillanDeLumiere(DeleteView):
    model = BillanDeLumiere
    template_name = 'Lumiere/delete_lumieres.html' 
    success_url = reverse_lazy('lumieres_list')

def BillanDeLumiereDetail(request, id):
    Lumieres_detail = BillanDeLumiere.objects.filter(pk=id)
    return render(request, 'Lumiere/lumieres_detail.html', {'Lumieres_detail':Lumieres_detail}) 

def BillanDeLumiereFilterEts(request, ets):
    Etablissements_list = Etablissements.objects.all()
    BillanLumiere_list_table = BillanDeLumiere.objects.filter(etablissements=ets)
    BillanLumiere_count_table = BillanDeLumiere.objects.filter(etablissements=ets).count()  
    return render(request, 'Lumiere/lumieres_filtre.html', {'Etablissements_list':Etablissements_list, 'ets':ets,
                                                         'BillanLumiere_list_table':BillanLumiere_list_table, 'BillanLumiere_count_table':BillanLumiere_count_table})

def export_lumiere_data(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        lumierebilan_resource = BillanDeLumiereResource()
        dataset = lumierebilan_resource.export()
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

    return render(request, 'Lumiere/lumieres_export.html')





    