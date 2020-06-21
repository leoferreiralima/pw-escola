from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView
from django.views.generic.edit import DeletionMixin,SingleObjectMixin,View
from django.http.response import HttpResponse
from http import HTTPStatus

from django.db.models import Q

from core.forms import ProfessorForm
from core.models import Professor


class DeleteViewWithoutRedirect(SingleObjectMixin,DeletionMixin,View):
  """
  Implemensts custom delete vie
  """
  def delete(self, request, *args, **kwargs):
    super().delete(request,args,kwargs)
    
    return HttpResponse(status= HTTPStatus.NO_CONTENT)

  def get_success_url(self):
    return "/"

class MainView (TemplateView):
  template_name= "main.html" 

class ProfessorListView (TemplateView):
  template_name= "professor/list.html"

class ProfessorModalCreateView (CreateView):
  template_name = "professor/modal/add-professor.html"
  model = Professor
  form_class = ProfessorForm
  success_url = reverse_lazy('professor-list')

class ProfessorModalUpdateView (UpdateView):
  template_name= "professor/modal/edit-professor.html"
  form_class = ProfessorForm
  success_url = reverse_lazy('professor-list')
  queryset = Professor.objects.all()

class ProfessorDeleteView(DeleteViewWithoutRedirect):
  model = Professor

class ProfessorTableListView(ListView):
  model = Professor
  template_name= "professor/table-list.html"

  def get_queryset(self):
    search = self.request.GET.get('search')
    if search : 
      filtro = None
      try:
        number_search = int(search)
        filtro = Q(matricula__exact=number_search)
      except:
        pass
      
      if not filtro:
        filtro = Q(nome__icontains=search)
      else:
        filtro |= Q(nome__icontains=search)

      code_titulacao = Professor.get_choice(search)

      filtro |= Q(endereco__icontains=search) | Q(telefone__icontains=search) | Q(titulacao = code_titulacao)

      return Professor.objects.filter(filtro)
    
    return Professor.objects.all()