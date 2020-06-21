from django.contrib import admin
from django.urls import path

from core.views import MainView,ProfessorListView,ProfessorModalCreateView
from core.views import ProfessorTableListView,ProfessorDeleteView,ProfessorModalUpdateView

urlpatterns = [
    path('', MainView.as_view(),name='main-page'),
    path('professor/', ProfessorListView.as_view(),name='professor-list'),
    path('professor/create/', ProfessorModalCreateView.as_view(),name='professor-create'),
    path('professor/list/',ProfessorTableListView.as_view(),name='professor-table-list'),
    path('professor/<int:pk>/edit', ProfessorModalUpdateView.as_view(),name='professor-edit'),
    path('professor/<int:pk>/delete', ProfessorDeleteView.as_view(),name='professor-delete'),
]
