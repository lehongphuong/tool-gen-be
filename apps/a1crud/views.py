from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# from .models import User
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
import requests
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import JsonResponse

from django.core import serializers

# Cache
from django.core.cache import cache

import json

# from models import User
from . import models

from django.db import connection

CUSTOMER_KEY = "customer.all"


def index(request):
    return render(request, "index.html", {"users": 1})

# *********************************************
# begin common


# convert cursor to json data
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


# execute query sql with cursor
def executeQuery(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)
    return data
# end common
# *********************************************

# *********************************************	
# begin Project	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from Project	
def create_data_project(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    obj = models.Project(**data)	
    obj.save()	
    return Response({"id": obj.id, "result": "ok"})
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from Project	
def read_data_project(request, format=None):	 
    return Response(serializers.serialize("json", models.Project.objects.all()))	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get update data from Project	
def update_data_project(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.Project(**data).save()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from Project	
def delete_data_project(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.Project(**data).delete()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from Project	
def find_data_project(request, format=None):	
    return Response(serializers.serialize("json", models.Project.objects.filter(pk=request.data['pk'])))	
	
# end Project	
# *********************************************	

# *********************************************	
# begin Class	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from Class	
def create_data_class(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    obj = models.Class(**data)	
    obj.save()	
    return Response({"id": obj.id, "result": "ok"})
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from Class	
def read_data_class(request, format=None):	
    return Response(serializers.serialize("json", models.Class.objects.all()))	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get update data from Class	
def update_data_class(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.Class(**data).save()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from Class	
def delete_data_class(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.Class(**data).delete()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from Class	
def find_data_class(request, format=None):	
    return Response(serializers.serialize("json", models.Class.objects.filter(pk=request.data['pk'])))	
	
# end Class	
# *********************************************	

# *********************************************	
# begin CRUD	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from CRUD	
def create_data_c_r_u_d(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    obj = models.CRUD(**data)	
    obj.save()	
    return Response({"id": obj.id, "result": "ok"})
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get all data from CRUD	
def read_data_c_r_u_d(request, format=None):	
    return Response(serializers.serialize("json", models.CRUD.objects.all()))	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get update data from CRUD	
def update_data_c_r_u_d(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.CRUD(**data).save()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from CRUD	
def delete_data_c_r_u_d(request, format=None):	
    data = json.loads(json.dumps(request.data))	
    models.CRUD(**data).delete()	
    return Response({"result": "ok"})	
	
	
@api_view(['POST'])	
@parser_classes((JSONParser,))	
# get delete data from CRUD	
def find_data_c_r_u_d(request, format=None):	
    return Response(serializers.serialize("json", models.CRUD.objects.filter(pk=request.data['pk'])))	
	
# end CRUD	
# *********************************************	

