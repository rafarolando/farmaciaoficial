from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib import  messages
from django.contrib.auth.decorators import permission_required, login_required

from farmaciasis.log_admin import admin_log_addition, admin_log_change
from farmaciasis.reportes import generar_pdf

from farmacia.models import Tipo, Turno, Farmacia
from farmacia.form import TipoForm, TurnoForm
from medicamentos.models import Medicamento

@permission_required('farmacia.add_tipo', login_url='/login')
def index_tipo(request):
    tipos = Tipo.objects.all()
    return render(request, 'tipos/index.html',{
        'tipos':tipos,
        })

@permission_required('farmacia.add_tipo', login_url='/login')
def new_tipo(request):
    if request.method == 'POST':
        formulario = TipoForm(request.POST)
        if formulario.is_valid():
            t = formulario.save()
            admin_log_addition(request, t, 'Tipo Creado')
            sms = "Tipo <strong>%s<strong> Creado Correctamente"% (t.nombre)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_tipo))
    else:
        formulario = TipoForm()
    return render(request, 'tipos/new_tipo.html',{
        'formulario':formulario,
    })


@permission_required('farmacia.change_tipo', login_url='/login')
def list_tipos_modificar(request):
    tipos = Tipo.objects.all()
    return render(request, 'tipos/list_modificar_tipo.html',{
        'tipos':tipos,
    })

@permission_required('farmacia.change_tipo', login_url='/login')
def update_tipo(request, tipo_id):
    tipo = get_object_or_404(Tipo, pk = tipo_id)
    if request.method == 'POST':
        formulario = TipoForm(request.POST, instance=tipo)
        if formulario.is_valid():
            t = formulario.save()
            admin_log_change(request, t, 'Tipo Modificado')
            sms = "Tipo <strong>$s<strong> Modificado Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(list_tipos_modificar))
    else:
        formulario = TipoForm(instance=tipo)
    return render(request, 'tipos/update_tipo.html',{
        'formulario':formulario,
    })


@login_required(login_url='/login')
def mis_turnos(request):
    farmacia = Farmacia.objects.filter(usuario = request.user)
    turnos = Turno.objects.filter(farmacia = farmacia)
    return render(request, 'turnos/index.html',{
        'turnos':turnos,
    })


@login_required(login_url='/login')
def new_turno(request):
    farmacia = Farmacia.objects.get(usuario = request.user)
    if request.method == 'POST':
        formulario  = TurnoForm(request.POST)
        if formulario.is_valid():
            t = formulario.save()
            t.farmacia = farmacia
            t.save()
            admin_log_addition(request, t, 'Turno Creado')
            sms = "Turno Creado Correctamente"
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(mis_turnos))
    else:
        formulario = TurnoForm()
    return render(request, 'turnos/new_turno.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def list_turnos_modificar(request):
    farmacia = Farmacia.objects.get(usuario = request.user)
    turnos = Turno.objects.filter(farmacia = farmacia)
    return render(request, 'turnos/list_modificar_turno.html',{
        'turnos':turnos,
    })

@login_required(login_url='/login')
def update_turno(request, turno_id):
    farmacia = Farmacia.objects.get(usuario = request.user)
    turno = get_object_or_404(Turno, pk = turno_id )
    if request.method == 'POST':
        formulario = TurnoForm(request.POST, instance=turno)
        if formulario.is_valid():
            t = formulario.save()
            t.farmacia = farmacia
            t.save()
            admin_log_change(request, t, 'Turno Modificado')
            sms = "Turno <strong>$s<strong> Modificado Correctamente"
            messages.success(request, sms)
            return  HttpResponseRedirect(reverse(list_turnos_modificar))
    else:
        formulario = TurnoForm(instance=turno)
    return render(request, 'turnos/update_turno.html',{
        'formulario':formulario,
    })

@login_required(login_url='/login')
def list_medicamentos_farmacias (request):
    farmacia = Farmacia.objects.get(usuario = request.user)
    medicamentos = Medicamento.objects.filter(farmacia = farmacia)
    return render(request, 'usuarios/list_medicamentos_farmacia.html',{
        'medicamentos':medicamentos,
    })