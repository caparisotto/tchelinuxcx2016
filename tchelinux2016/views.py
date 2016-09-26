# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import os,sys,psycopg2.extras

# Create your views here.

def inicial(request):
	titulo = "Precisamos falar sobre Administração de Sistemas"
	proximo = "/slide2/"
        return render_to_response("capa.html",{'titulo': titulo, 'proximo': proximo})

def slide2(request):
	number = 2
	anterior = "/"
	proximo = "/slide3/"
	titulo = "Sysadmin Folgado"
        return render_to_response("slide2.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def final(request):
	titulo = "Perguntas?"
	anterior = "/slide12/"
        return render_to_response("ultimo.html",{'titulo': titulo, 'anterior': anterior})
