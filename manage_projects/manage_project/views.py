from django.shortcuts import render
from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Project, Technologie
from .serializers import ProjectSerializer, TechnologieSerializar, ProjectByTechnologieSerializer

# Create your views here.

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #filtragem
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['name', 'date_init']
    #autentificação 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TecnologieViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializar

class ListProjectsByTecnologiesView(generics.ListAPIView):
    #sobrescrever queryset
    "lista os projetos que ultilizam a tecnologia"
    def get_queryset(self):
        queryset = Project.objects.filter(technologie_id=self.kwargs['pk'])
        return queryset
    serializer_class = ProjectByTechnologieSerializer


   

