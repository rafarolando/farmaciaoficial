from django.forms import ModelForm, TextInput

from farmacia.models import Farmacia, Tipo, Turno

class FarmaciaForm(ModelForm):
    class Meta:
        model = Farmacia
        fields = '__all__'
        exclude = {'usuario'}


class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'

class  TurnoForm(ModelForm):
    class Meta:
        model = Turno
        exclude = ['farmacia']
        widgets  = {'fecha':TextInput(attrs={'type':'date'})}