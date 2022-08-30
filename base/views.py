from django.shortcuts import render
import json
import requests
from urllib import parse, request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Search

# Create your views here.

url = "http://api.giphy.com/v1/gifs/search"

def func(json_object):
    retVal=[]
    for objs in json_object["data"]:
        if "url" in objs:
            retVal.append(objs["url"])
    return retVal


@api_view(['GET'])
def SearchGif(request,query):
    
    params = parse.urlencode({
        "q": query,
        "api_key": "itS8PLUPfStYsCOMtyQCvYoxYIHlkYFV",
        "limit": "5"
    })
    response = requests.get(url, params=params)
    json_data = json.loads(response.text) 
    Search.objects.create(search_term=query, response=func(json_data))
   
    return Response(func(json_data))    

@api_view(['GET'])
def getData(request):
    return Response(Search.objects.all().values())


