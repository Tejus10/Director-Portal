from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createinternalletter/',views.internal_creation_form,name='internal_letter_form'),
    path('createexternalletter/',views.external_creation_form,name='external_letter_form'),
    path('edit_external/<letter_id>',views.edit_external,name='edit_external'),
    path('edit_internal/<letter_id>',views.edit_internal,name='edit_internal'),
    path('files_to_me/',views.files_referred,name='files_referred'),
    path('details_internal/<letter_id>',views.detail_internal,name='detail_internal'),
    path('details_external/<letter_id>',views.detail_external,name='detail_external'),
    
]
