from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    # Examples:
    # url(r'^$', 'farmacia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^rafael/$', 'usuarios.views.home'),
    url(r'^$', 'usuarios.views.base'),

    #USUARIOS
    url(r'^usuario/new/$', 'usuarios.views.new_user'),
    url(r'^login/$', 'usuarios.views.logget_in'),
    url(r'^usuario/perfil/$', 'usuarios.views.perfil'),
    url(r'^logout/$', 'usuarios.views.salir'),
    url(r'^usuario/update/perfil/$', 'usuarios.views.update_perfil'),

    #TIPOS
    url(r'^tipo/$', 'farmacia.views.index_tipo'),
    url(r'^tipo/new/$', 'farmacia.views.new_tipo'),
    url(r'^tipo/list/modificar/$', 'farmacia.views.list_tipos_modificar'),
    url(r'^tipo/(?P<tipo_id>\d+)/$', 'farmacia.views.update_tipo'),


    #TURNOS
    url(r'^mis/turno/$', 'farmacia.views.mis_turnos'),
    url(r'^turno/new/$', 'farmacia.views.new_turno'),
    url(r'^turno/list/modificar/$', 'farmacia.views.list_turnos_modificar'),
    url(r'^turno/(?P<turno_id>\d+)/$', 'farmacia.views.update_turno'),

    #COMPUESTOS
    url(r'^compuestos/$', 'medicamentos.views.index_compuesto'),
    url(r'^compuestos/new/$', 'medicamentos.views.new_compuesto'),
    url(r'^compuestos/list/modificar/$', 'medicamentos.views.list_modificar_compuesto'),
    url(r'^compuestos/(?P<compuesto_id>\d+)/$', 'medicamentos.views.update_compuesto'),

    #PROVEEDORES
    url(r'^proveedor/$', 'medicamentos.views.index_proveedor'),
    url(r'^proveedor/new/$', 'medicamentos.views.new_proveedor'),
    url(r'^proveedor/list/modificar/$', 'medicamentos.views.list_proveedor_modificar'),
    url(r'^proveedor/(?P<proveedor_id>\d+)/$', 'medicamentos.views.update_proveedor'),

    #UNIDADES
    url(r'^unidad/$', 'medicamentos.views.index_unidad'),
    url(r'^unidad/new/$', 'medicamentos.views.new_unidad'),
    url(r'^unidad/list/modificar/$', 'medicamentos.views.list_modificar_unidad'),
    url(r'^unidad/(?P<unidad_id>\d+)/$', 'medicamentos.views.update_unidad'),

    #MEDICAMENTOS
    url(r'^medicamento/$', 'medicamentos.views.index_medicamento'),
    url(r'^medicamento/new/$', 'medicamentos.views.new_medicamento'),
    url(r'^medicamento/list/modificar/$', 'medicamentos.views.list_modificar_medicamento'),
    url(r'^medicamento/(?P<medicamento_id>\d+)/$', 'medicamentos.views.update_medicamento'),
    url(r'^medicamento/lista/farmacia/$', 'farmacia.views.list_medicamentos_farmacias'),

)
