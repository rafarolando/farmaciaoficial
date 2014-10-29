from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib import  messages
from django.contrib.auth.decorators import permission_required, login_required

from farmaciasis.log_admin import admin_log_addition, admin_log_change
from farmaciasis.reportes import generar_pdf

from medicamentos.models import Proveedor,Compuesto,Unidad,Medicamento
from medicamentos.form  import ProveedorForm, CompuestoForm, UnidadForm, MedicamentoForm

@permission_required('medicamento.add_proveedor', login_url='/login')
def index_proveedor (request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/index_proveedor.html',{
        'proveedores':proveedores,
    })

@permission_required('medicamentos.add_proveedor', login_url='/login')
def new_proveedor (request):
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            p = formulario.save()
            admin_log_addition(request,p,'Proveedor Creado')
            sms = "Proveedor <strong>%s</strong> Creado Correctamente"%(p.nombre)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(index_proveedor))
    else:
        formulario = ProveedorForm()
    return render(request, 'proveedores/new_proveedor.html',{
        'formulario':formulario,
    })

@permission_required('medicamentos.change_proveedor', login_url='/login')
def list_proveedor_modificar (request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/list_modificar_proveedor.html',{
        'proveedores':proveedores,
    })

@permission_required('medicamentos.change_proveedor', login_url='/login')
def update_proveedor (request, proveedor_id):
    proveedor = get_object_or_404(request, pk = proveedor_id)
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST, instance=proveedor)
        if formulario.is_valid():
            p = formulario.save()
            admin_log_change(request,p,'Proveedor Modificado')
            sms = "Proveedor <strong>$s</strong> Modificado Correctamente"%(p.nombre)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(list_proveedor_modificar))
    else:
        formulario = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/update_proveedor.html',{
        'formulario':formulario,
    })

@permission_required('medicamentos.add_unidad', login_url='/login')
def index_unidad (request):
    unidades = Unidad.objects.all()
    return render(request, 'unidades/index_unidad.html',{
        'unidades':unidades,
    })

@permission_required('medicamentos.add_unidad', login_url='/login')
def new_unidad (request):
    if request.method == 'POST':
        formulario = UnidadForm(request.POST)
        if formulario.is_valid():
            u = formulario.save()
            admin_log_addition(request,u,'Unidad Creada')
            sms = "Unidad <strong>%s</strong> Creada Correctamente"%(u.sigla)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(index_unidad))
    else:
        formulario = UnidadForm()
    return render(request, 'unidades/new_unidad.html',{
        'formulario':formulario,
    })


@permission_required('medicamentos.change_unidad', login_url='/login')
def list_modificar_unidad (request):
    unidades = Unidad.objects.all()
    return  render(request, 'unidades/list_modificar_unidad.html',{
        'unidades':unidades,
    })


@permission_required('medicamentos.change_unidad', login_url='/login')
def update_unidad (request, unidad_id):
    unidad = get_object_or_404(request, pk = unidad_id)
    if request.nethod == 'POST':
        formulario = UnidadForm(request.POST, instance=unidad)
        if formulario.is_valid():
            u = formulario.save()
            admin_log_change(request,u,'Unidad Modificada')
            sms = "Unidad <strong>%s</strong> Modificada Correctamente"%(u.sigla)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(list_modificar_unidad))
    else:
        formulario = UnidadForm(instance=unidad)
    return render(request, 'unidades/update_unidad.html',{
        'formulario':formulario,
    })

#@permission_required('medicamentos.add.compuesto', login_url='/login')
def index_compuesto (request):
    compuestos = Compuesto.objects.all()
    return render(request, 'compuestos/index_compuesto.html',{
        'compuestos':compuestos,
    })

@permission_required('medicamentos.add.compuesto', login_url='/login')
def new_compuesto(request):
    if request.method == 'POST':
        formulario = CompuestoForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_addition(request,c,'Compuesto Creado')
            sms = "Compuesto <strong>%s</strong> Creado Correctamente"%(c.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_compuesto))
    else:
        formulario = CompuestoForm()
    return render(request, 'compuestos/new_compuesto.html',{
        'formulario':formulario,
    })

@permission_required('medicamentos.change_compuesto', login_url='/login')
def list_modificar_compuesto (request):
    compuestos = Compuesto.objects.all()
    return render (request, 'compuestos/list_modificar_compuesto.html',{
        'compuestos':compuestos,
    })

@permission_required('medicamentos.change_compuesto', login_url='/login')
def update_compuesto (request, compuesto_id):
    compuesto = get_object_or_404(request, pk = compuesto_id)
    if request.method == 'POST':
        formulario = CompuestoForm(request.POST, instance=compuesto)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_change(request,c,'Compuesto Modificado')
            sms = "Compuesto <strong>%s</strong> Modificado Correctamente"%(c.nombre)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(list_modificar_compuesto))
    else:
        formulario = CompuestoForm(instance=compuesto)
    return render(request, 'compuestos/update_compuesto.html',{
        'fomrulario':formulario,
    })

@permission_required('medicamentos.add_medicamento', login_url='/login')
def index_medicamento (request):
    medicamentos = Medicamento.objects.all()
    return render (request, 'medicamentos/index_medicamento.html',{
        'medicamentos':medicamentos,
    })

@permission_required('medicamentos.add_medicamento', login_url='/login')
def new_medicamento (request):
    if request.method == 'POST':
        formulario = MedicamentoForm(request.POST)
        if formulario.is_valid():
            m = formulario.save()
            admin_log_addition(request,m,'Medicamento Creado')
            sms = "Medicamento <strong>%s</strong> Creado Correctamente"%(m.nombre)
            messages.success(request, sms)
            return  HttpResponseRedirect(reverse(index_medicamento))
    else:
        formulario = MedicamentoForm()
    return render (request, 'medicamentos/new_medicamento.html',{
        'formulario':formulario,
    })

@permission_required('medicamentos.change_medicamento', login_url='/login')
def list_modificar_medicamento(request):
    medicamentos = Medicamento.objects.all()
    return render (request, 'medicamentos/list_modificar_medicamento.html',{
        'medicamentos':medicamentos,
    })

permission_required('medicamentos.change_medicamento', login_url='/login')
def update_medicamento (request, medicamento_id):
    medicamentos = get_object_or_404(request, pk = medicamento_id)
    if request.method == 'POST':
        formulario = MedicamentoForm(request.POST, instance = medicamentos)
        if formulario.is_valid():
            m = formulario.save()
            admin_log_change(request,m,'Medicamento Modificado')
            sms = "Medicamento <strong>%s</strong> Modificado Correctamente"%(m.nombre)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(list_modificar_medicamento))
    else:
        formulario = MedicamentoForm(instance=medicamentos)
    return render(request, 'medicamentos/update_medicamento.html',{
        'formulario':formulario,
    })
