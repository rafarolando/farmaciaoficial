__author__ = 'Rafael'

from django.http import HttpResponse
from django.conf import settings
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
import os

def generar_pdf(html):
    result = StringIO.StringIO()
    links = lambda uri,rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-16")),result, link_callback=links)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))