from django.forms import ModelForm, TextInput

from medicamentos.models import Compuesto,Proveedor,Unidad,Medicamento

class CompuestoForm (ModelForm):
    class Meta:
        model = Compuesto
        fields = '__all__'


class ProveedorForm (ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class UnidadForm (ModelForm):
    class Meta:
        model = Unidad
        fields = '__all__'


class MedicamentoForm (ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'



