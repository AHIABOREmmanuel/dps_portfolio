from django.db import models
from django.utils import timezone

# Create your models here.


class Realisations(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField()
    lien=models.CharField(max_length=255)
    satut= models.CharField(max_length=255)


class Offre(models.Model):
    image = models.ImageField(null=False, upload_to='Offre',)
    nom=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    periode_validite=models.CharField(max_length=255)


class Publication(models.Model):
    images = models.ImageField(null=False, upload_to='Publication',)
    titre=models.CharField(max_length=255)
    description=models.TextField()
    auteur=models.CharField(max_length=255)
    
class Commentaires(models.Model):
    auteur= models.CharField(max_length=255)
    message=models.TextField()
    publication=models.ForeignKey(Publication, on_delete=models.CASCADE)




class Temoignage(models.Model):
    nom=models.CharField(max_length=255)
    texte=models.CharField(max_length=255)


class MembreEquipe(models.Model):
    nom=models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    bio=models.TextField()
    photo=models.ImageField(null=False, upload_to='MembreEquipe',)

class Service(models.Model):
    image = models.ImageField(null=False, upload_to='Service',)
    nom=models.CharField(max_length=255)
    descritption=models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)


#class Abonnement(models.Model):
    #nom=models.CharField(max_length=255)
    #descritption=models.TextField()
    #prix = models.DecimalField(max_digits=8, decimal_places=2)