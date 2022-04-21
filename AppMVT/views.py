from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from contextvars import Context
from pipes import Template
from re import template
from django.template import Template, Context, loader
from AppMVT.models import Familia

def familia(self):

    familiar1 = Familia(nombre = "Bianca DAlessandro", edad = 24, fechaNacimiento = "1997-05-12")
    familiar1.save()
    familiar2 = Familia(nombre = "Javier DAlessandro", edad = 52, fechaNacimiento = "1970-11-27")
    familiar2.save()
    familiar3 = Familia(nombre = "Santiago DAlessandro", edad = 8, fechaNacimiento = "2013-10-9")
    familiar3.save()
    diccionario = {"name1":familiar1.nombre,"age1":familiar1.edad,"bornDate1":familiar1.fechaNacimiento,"name2":familiar2.nombre,"age2":familiar2.edad,"bornDate2":familiar2.fechaNacimiento,"name3":familiar3.nombre,"age3":familiar3.edad,"bornDate3":familiar3.fechaNacimiento,}

    plantilla = loader.get_template("template.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)