from django import forms
from django.forms import fields, widgets
from .models import Participants, Etablissements, BillanDeLumiere
from Supports.models import Sexe

choices = Sexe.objects.all().values_list('name' , 'name')
choice = Etablissements.objects.all().values_list('name' , 'name')

choice_list = []
for item in choices:
    choice_list.append(item)


class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissements
        fields = ('name', 'auteur')  
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class': 'form-control'}),
        }


class ParticipantFrom(forms.ModelForm):
    class Meta:
        model = Participants
        fields =  ('nom', 'prenom', 'sexe', 'age', 'numero', 'email', 'eglise_frequente', 'classe', 'residence', 'probleme_particulier', 'projets', 'etablissement', 'dirigeant', 'auteur') 

        
        widgets = {
            'nom' : forms.TextInput(attrs={'class':'form-control'}),
            'prenom' : forms.TextInput(attrs={'class':'form-control'}),
            'sexe' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'numero' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'eglise_frequente' : forms.TextInput(attrs={'class':'form-control'}),
            'classe' : forms.TextInput(attrs={'class':'form-control'}),
            'etablissement' : forms.TextInput(attrs={'class':'form-control'}),
            'residence' : forms.TextInput(attrs={'class':'form-control'}),
            'dirigeant' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
        }




class BillanDeLumiereFrom(forms.ModelForm):
    class Meta:
        model = BillanDeLumiere
        fields = ('titre', 'etablissements', 'enseignant', 'numbre_de_fille', 'numbre_de_garcon', 'rapports_suggestions', 'date', 'auteur')

        
        widgets = {
            'titre' : forms.TextInput(attrs={'class':'form-control'}),
            'etablissements' : forms.Select(choices=choice, attrs={'class':'form-control'}),
            'enseignant' : forms.TextInput(attrs={'class':'form-control'}),
            'numbre_de_fille' : forms.TextInput(attrs={'class':'form-control'}),
            'numbre_de_garcon' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.TextInput(attrs={'class':'form-control'}),
            'auteur' : forms.Select(attrs={'class':'form-control'}),
            
        }








