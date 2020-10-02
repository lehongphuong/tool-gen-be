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

from ultil.u1core import GenSourceCore
from ultil.u2database import GenSourceDatabase
from ultil.u3backend import GenSourceBackend
from ultil.u4frontend import GenSourceFrontend
from ultil.u5cicd import GenCICD
core_gen = GenSourceCore()
gen_database = GenSourceDatabase()
gen_backend = GenSourceBackend()
gen_frontend = GenSourceFrontend()
gen_cicd = GenCICD()

# Cache
from django.core.cache import cache

import json

# from models import User
from . import models

from django.db import connection

CUSTOMER_KEY = "customer.all"


def index(request):
    return render(request, "index.html", {"users": 1})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from Customer
def gencode(request, format=None):
    data = json.loads(json.dumps(request.data))
    idproject = data["idproject"]
    gen_database.gen_database_mysql(idproject)
    gen_backend.gen_backend_php(idproject)
    gen_frontend.gen_frontend_angular(idproject)
    project_name = gen_cicd.gen_docker_angular(idproject)
    download_link = core_gen.zip_project(project_name)
    return Response({"result": download_link})


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
# begin Customer
@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from Customer
def createDataCustomer(request, format=None):
    data = json.loads(json.dumps(request.data))
    obj = models.Customer(**data)
    obj.save()
    cache.delete(CUSTOMER_KEY)
    return Response({"id": obj.id, "result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get all data from Customer
def readDataCustomer(request, format=None):
    customers = models.Customer.objects.all()
    # customers = cache.get(CUSTOMER_KEY)
    # if not customers:
    #     customers = models.Customer.objects.all()
    #     cache.set(CUSTOMER_KEY, customers)

    return Response(serializers.serialize("json", customers))


@api_view(['POST'])
@parser_classes((JSONParser,))
# get update data from Customer
def updateDataCustomer(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.Customer(**data).save()
    cache.delete(CUSTOMER_KEY)
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from Customer
def deleteDataCustomer(request, format=None):
    data = json.loads(json.dumps(request.data))
    models.Customer(**data).delete()
    cache.delete(CUSTOMER_KEY)
    return Response({"result": "ok"})


@api_view(['POST'])
@parser_classes((JSONParser,))
# get delete data from Customer
def findDataCustomer(request, format=None):
    return Response(serializers.serialize("json", models.Customer.objects.filter(pk=request.data['pk'])))


@api_view(['POST'])
@parser_classes((JSONParser,))
# find data by status
def find_custommer_by_status(request, format=None):
    if(request.data['status'] < 4):
        return Response(serializers.serialize("json", models.Customer.objects.filter(status=request.data['status'])))
    else:
        return Response(serializers.serialize("json", models.Customer.objects.all()))


@api_view(['POST'])
@parser_classes((JSONParser,))
# find data customer from two date
def find_custommer_between_date(request, format=None):
    customer = models.Customer.objects.filter(start_date__gte=request.data['start_date'], start_date__lte=request.data['end_date']) | models.Customer.objects.filter(end_date__gte=request.data['start_date'], end_date__lte=request.data['end_date'])
    return Response(serializers.serialize("json", customer))

# end Customer
# *********************************************
