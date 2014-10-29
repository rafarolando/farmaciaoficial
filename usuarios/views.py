from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from farmacia.form import FarmaciaForm
from farmacia.models import Farmacia

def base(request):
    return render_to_response('base.html', {

    }, context_instance=RequestContext(request))


def new_user(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        formulariofar = FarmaciaForm(request.POST)
        if formulario.is_valid() and formulariofar.is_valid():
            u = formulario.save()
            u.is_active = False
            f = formulariofar.save()
            f.usuario = u
            f.save()
            u.save()
            sms = "<h4>Se registro correctamente %s </h4>  " % (u.username)
            messages.success(request,sms, )
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
        formulariofar = FarmaciaForm()
    return render_to_response('usuarios/new_user.html', {
        'formulario': formulario,
        'formulariofar':formulariofar,
    }, context_instance=RequestContext(request))

def logget_in(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse(perfil))
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        acceso = authenticate(username = usuario, password = clave)
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                sms = 'Sesion Iniciada Correctamente'
                messages.success(request,sms, )
                #messages.info(request,sms, )
                #messages.warning(request,sms, )
                #messages.error(request,sms, )
                #messages.add_message(request, messages.INFO, sms)
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                else:
                    return HttpResponseRedirect(reverse(perfil))
            else:
                sms = 'Cuenta No Esta Activa'
                messages.warning(request,sms, )
                return HttpResponseRedirect(reverse(logget_in))
        else:
            sms = 'Ususario No Registrado'
            messages.error(request,sms, )
            return HttpResponseRedirect(reverse(logget_in))
    else:
        formulario = AuthenticationForm()
    return render_to_response('usuarios/login.html',{
        'formulario':formulario,
    }, context_instance = RequestContext(request))


@login_required(login_url='/login')
def perfil(request):
    return render_to_response('usuarios/perfil.html',{

    },   context_instance = RequestContext(request))

@login_required(login_url='/login')
def salir(request):
    sms = 'Sesion Terminada'
    messages.add_message(request, messages.INFO, sms)
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login')
def update_perfil (request):
    farmacia = Farmacia.objects.get(usuario = request.user)
    if request.method == 'POST':
        formulariofar = FarmaciaForm(request.POST, request.FILES, instance=farmacia)
        if formulariofar.is_valid():
            f = formulariofar.save()
            sms = "<h4>Se registro correctamente %s </h4>  " % (f.usuario.username)
            messages.success(request,sms, )
            return HttpResponseRedirect('/')
    else:
        formulariofar = FarmaciaForm(instance=farmacia)
    return render_to_response('usuarios/update_perfil.html', {
        'formulariofar':formulariofar,
    }, context_instance=RequestContext(request))