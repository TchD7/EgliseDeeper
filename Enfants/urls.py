from django.urls import path
from .views import EnfantList, AddEnfants, EnfantsDetail, EditeEnfants, DeleteEnfants, Search_Enfants, \
        FilterEnfantsDistrict, FilterEnfantsGroupe, FilterEnfantsRegion, FilterEnfantsSexe, FilterEnfantsDistrictTable,\
        FilterEnfantsGroupeTable, EnfantTableList, export_data


urlpatterns = [
    path('add_enfant', AddEnfants.as_view(), name="add_enfants"),
    path('enfants', EnfantList.as_view(), name="enfants_list"),
    path('enfants_table_list', EnfantTableList, name="enfants_table_list"),
    path('enfants/<int:id>', EnfantsDetail, name="enfant_detail"),
    path('enfants/<int:pk>/edit', EditeEnfants.as_view(), name="edite_enfants"),
    path('enfants/<int:pk>/delete', DeleteEnfants.as_view(), name="delete_enfants"),
    path('enfants_search', Search_Enfants, name="enfants_search"),
    path('district/<str:dist>/', FilterEnfantsDistrict, name="enfants_district"),
    path('groupe/<str:group>/', FilterEnfantsGroupe, name="enfants_groupe"),
    path('region/<str:regs>', FilterEnfantsRegion, name="enfants_region"),
    path('sexe/<str:sexs>/', FilterEnfantsSexe, name="enfants_sexe"),
    path('district_table/<str:dist>/', FilterEnfantsDistrictTable, name="enfants_district_table"),
    path('groupe_table/<str:group>/', FilterEnfantsGroupeTable, name="enfants_groupe_table"),
    
    path('enfants_export', export_data, name="enfants_export"),
]




