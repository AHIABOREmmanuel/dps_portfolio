from rest_framework import serializers
from api.models import *




class RealisationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realisations
        fields = '__all__'


class OffreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'


class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class TemoignageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temoignage
        fields = '__all__'


class MembreEquipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MembreEquipe
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CommentairesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commentaires
        fields = '__all__'



