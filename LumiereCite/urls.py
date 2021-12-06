from django.urls import path
from .views import ParticipantList, AddParticipants, ParticipantsDetail, EditParticipant, DeleteParticipant, \
    AddEtablissement, EtsList, EditEtablissement, DeleteEtablissement, \
        BillanDeLumiereList, AddBillanDeLumiere, EditBillanDeLumiere, DeleteBillanDeLumiere, BillanDeLumiereDetail, \
            BillanDeLumiereFilterEts, export_lumiere_data, export_ecoles_data, export_participant_data


urlpatterns = [
    path('participants', ParticipantList.as_view(), name='participants_list'),
    path('add_participants', AddParticipants.as_view(), name='add_participants'),
    path('participants/<int:id>', ParticipantsDetail, name='participants_detail'),
    path('participants/<int:pk>/edit', EditParticipant.as_view(), name='edit_participants'),
    path('participants/<int:pk>/delete', DeleteParticipant.as_view(), name='delete_participants'),
    path('export_participant_data', export_participant_data, name='export_participant_data'),
    
    path('add_etablissement', AddEtablissement.as_view(), name='add_etablissement'),
    path('etablissements', EtsList.as_view(), name='etablissements_list'),
    path('etablissements/<int:pk>/edit', EditEtablissement.as_view(), name='edit_etablissements'),
    path('etablissements/<int:pk>/delete', DeleteEtablissement.as_view(), name='delete_etablissements'),
    path('export_ecoles_data', export_ecoles_data, name='export_ecoles_data'),
    
    path('add_lumieres', AddBillanDeLumiere.as_view(), name='add_lumieres'),
    path('lumieres', BillanDeLumiereList.as_view(), name='lumieres_list'),
    path('lumieres/<int:pk>/edit', EditBillanDeLumiere.as_view(), name='edit_lumieres'),
    path('lumieres/<int:pk>/delete', DeleteBillanDeLumiere.as_view(), name='delete_lumieres'),
    path('lumieres/<int:id>', BillanDeLumiereDetail, name='lumieres_detail'),
    path('lumieres_filtre/<str:ets>', BillanDeLumiereFilterEts, name='lumieres_filtre_ets'),
    path('export_lumiere_data', export_lumiere_data, name='export_lumiere_data'),
]


