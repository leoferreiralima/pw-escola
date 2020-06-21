from django import forms

from core.models import Professor

class ProfessorForm(forms.ModelForm):
  matricula = forms.IntegerField(widget = forms.HiddenInput(),required=False)
  class Meta:
    model = Professor
    fields = "__all__"