from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Realisations', RealisationsViewSet, basename='realisations')
router.register('Offre', OffreViewSet, basename='offre')
router.register('Publication', PublicationViewSet, basename='publication')
router.register('Temoignage', TemoignageViewSet, basename='temoignage')
router.register('MembreEquipe', MembreEquipeViewSet, basename='membreequipe')
router.register('Service', ServiceViewSet, basename='service')
router.register('Commentaires', CommentairesViewSet, basename='commentaires')

router.register('admin/Realisations', RealisationsAdminViewSet, basename='admin-realisations')
router.register('admin/Offre', OffreAdminViewSet, basename='admin-offre')
router.register('admin/Publication', PublicationAdminViewSet, basename='admin-publication')
router.register('admin/Temoignage', TemoignageAdminViewSet, basename='admin-temoignage')
router.register('admin/MembreEquipe', MembreEquipeAdminViewSet, basename='admin-membreequipe')
router.register('admin/Service', ServiceAdminViewSet, basename='admin-service')
router.register('admin/Commentaires', CommentairesAdminViewSet, basename='admin-commentaires')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
   
# ]