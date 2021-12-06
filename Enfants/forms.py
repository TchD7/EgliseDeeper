from django import forms
from django.forms import fields, widgets
from Enfants.models import EnfantsPost
from Eglises.models import Districts, Groups
from Supports.models import Sexe, Region, Reponses

choices = Districts.objects.all().values_list('name', 'name')
choice = Groups.objects.all().values_list('name', 'name')
reg_choice = Region.objects.all().values_list('name', 'name')
sexs_choice = Sexe.objects.all().values_list('name', 'name')
reponse = Reponses.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

 
class EnfantsPostForm(forms.ModelForm):
    class Meta:
        model = EnfantsPost
        fields = ('nom', 'prenom', 'date_de_naissance', 'lieu_de_naissance', 'residence', 'district', 'groupe', 
                  'region', 'classe', 'sexe', 'groupe_sanguin', 'rhesus', 'role_dans_leglise', 'avec_qui_vit_il', 
                  'nombre_de_freres', 'les_freres_sont_ils_dans_leglise', 'nom_des_freres', 'nombre_de_soeurs', 
                  'les_soeurs_sont_elles_dans_leglise', 'nom_des_soeurs', 'nom_des_parentes', 'les_parents_sont_ils_dans_leglise', 
                  'dirigeant', 'distance_maison_district', 'distance_maison_ecole', 
                  'nom_des_parents_ou_tuteurs', 'contact', 'contact_whatsapp', 'description_sur_l_enfant', 
                  'enfant_images', 'auteur')  



        widgets = {
            
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_de_naissance' : forms.DateInput(attrs={'class': 'form-control'}),
            'lieu_de_naissance' : forms.TextInput(attrs={'class': 'form-control'}),
            'residence' : forms.TextInput(attrs={'class': 'form-control'}),
            'district' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'groupe' : forms.Select(choices=choice, attrs={'class': 'form-control'}),
            'region' : forms.Select(choices=reg_choice, attrs={'class': 'form-control'}),
            'classe' : forms.TextInput(attrs={'class': 'form-control'}),
            'sexe' : forms.Select(choices=sexs_choice, attrs={'class': 'form-control'}),
            
            'groupe_sanguin' : forms.TextInput(attrs={'class': 'form-control'}),
            'rhesus' : forms.TextInput(attrs={'class': 'form-control'}),
            'role_dans_leglise' : forms.TextInput(attrs={'class': 'form-control'}),
            'avec_qui_vit_il' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_freres_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_freres' : forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_de_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_soeurs_sont_elles_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'nom_des_soeurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_des_parentes' : forms.TextInput(attrs={'class': 'form-control'}),
            'les_parents_sont_ils_dans_leglise' : forms.Select(choices=reponse, attrs={'class': 'form-control'}),
            'dirigeant' : forms.TextInput(attrs={'class': 'form-control'}),
            
            'distance_maison_district' : forms.TextInput(attrs={'class': 'form-control'}),
            'distance_maison_ecole' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_des_parents_ou_tuteurs' : forms.TextInput(attrs={'class': 'form-control'}),
            'contact' : forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_whatsapp' : forms.NumberInput(attrs={'class': 'form-control'}),
            'auteur' : forms.Select(attrs={'class': 'form-control'}),
            
        }





