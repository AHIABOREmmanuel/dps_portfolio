from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from api.models import *
from backend.models import *
from api.serializers import *

# Create your views here.

# Read
class RealisationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Realisations.objects.all()
    serializer_class = RealisationsSerializer
    
# Read
class OffreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
   
# Read
class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    
# Read
class TemoignageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Temoignage.objects.all()
    serializer_class = TemoignageSerializer
    
# Read
class MembreEquipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MembreEquipe.objects.all()
    serializer_class = MembreEquipeSerializer
    
# Read
class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
   

# Read
class CommentairesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commentaires.objects.all()
    serializer_class = CommentairesSerializer
    


# admin endpoints

class RealisationsAdminViewSet(viewsets.ModelViewSet):
    queryset = Realisations.objects.all()
    serializer_class = RealisationsSerializer
    permission_classes = [permissions.IsAdminUser]

class OffreAdminViewSet(viewsets.ModelViewSet):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    permission_classes = [permissions.IsAdminUser]

class PublicationAdminViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAdminUser]

class TemoignageAdminViewSet(viewsets.ModelViewSet):
    queryset = Temoignage.objects.all()
    serializer_class = TemoignageSerializer
    permission_classes = [permissions.IsAdminUser]

class MembreEquipeAdminViewSet(viewsets.ModelViewSet):
    queryset = MembreEquipe.objects.all()
    serializer_class = MembreEquipeSerializer
    permission_classes = [permissions.IsAdminUser]

class ServiceAdminViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]


class CommentairesAdminViewSet(viewsets.ModelViewSet):
    queryset = Commentaires.objects.all()
    serializer_class = CommentairesSerializer
    permission_classes = [permissions.IsAdminUser]
