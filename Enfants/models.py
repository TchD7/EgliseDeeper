from django.db import models
from django.contrib.auth.models import User
from Supports.models import Ocupation, Roles
from ckeditor.fields import RichTextField
from django.urls import reverse


class EnfantsPost(models.Model):
    nom = models.CharField(max_length=150) 
    prenom = models.CharField(max_length=150)
    date_de_naissance = models.DateField(max_length=150, auto_now_add=False)
    lieu_de_naissance = models.CharField(max_length=150)
    residence = models.CharField(max_length=150)
    district = models.CharField(max_length=150) 
    groupe = models.CharField(max_length=150) 
    region = models.CharField(max_length=150) 
    classe = models.CharField(max_length=150) 
    sexe = models.CharField(max_length=150)
    
    groupe_sanguin = models.CharField(max_length=25)
    rhesus = models.CharField(max_length=10)
    role_dans_leglise = models.ForeignKey(Roles, on_delete=models.CASCADE)
    talents_de_l_enfant =models.CharField(max_length=400, blank=True, null=True)
    avec_qui_vit_il = models.CharField(max_length=100)
    nombre_de_freres = models.IntegerField()
    les_freres_sont_ils_dans_leglise = models.CharField(max_length=100)
    nom_des_freres = models.CharField(max_length=500, blank=True, null=True)
    nombre_de_soeurs = models.IntegerField()
    les_soeurs_sont_elles_dans_leglise = models.CharField(max_length=100)
    nom_des_soeurs = models.CharField(max_length=500, blank=True, null=True) 
    nom_des_parentes = models.CharField(max_length=400) 
    les_parents_sont_ils_dans_leglise = models.CharField(max_length=100) 
    dirigeant = models.CharField(max_length=300)
    
    distance_maison_district = models.CharField(max_length=100, blank=True, null=True)
    distance_maison_ecole = models.CharField(max_length=100, blank=True, null=True)
    nom_des_parents_ou_tuteurs = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    contact_whatsapp = models.CharField(max_length=150, blank=True, null=True)
    description_sur_l_enfant = RichTextField()
    enfant_images = models.ImageField(blank=True, null=True, upload_to='images/enfant')
    add_date = models.DateField(max_length=150, auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom + ' ' + self.prenom
    
    def get_absolute_url(self):
        return reverse('enfants_list')
    
    
    




