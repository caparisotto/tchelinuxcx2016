# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import os,sys,psycopg2.extras

# Create your views here.

#def capa(request):
#        return render_to_response("capa.html")

def sobre(request):
        return render_to_response("sobre.html")

def prints(request,img):
        anterior=int(img)-1
        proximo=int(img)+1
        
        if img == "1":
            anterior = 1
        elif img == "21":
            proximo = 21

        imagem="tche"+img+".png"
        return render_to_response("prints.html", {'imagem': imagem, 'anterior': anterior, 'proximo': proximo})

def fontes(request):
        return render_to_response("fontes.html")

def conclusao(request):
        return render_to_response("conclusao.html")
