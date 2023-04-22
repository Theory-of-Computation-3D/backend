from django.http import JsonResponse, HttpResponse
import json
from getData import Wat 
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.load(body)
    except:
        pass

    return JsonResponse({"what": "its working huh"})

def select(request, *args, **kwargs):
    params = request.GET.get('Select(number)', '')
    data = {}
    data = json.loads(params)
    recv = Wat()
    recv.province = data
    recv.select_province(recv.province)
    return JsonResponse(recv.data, safe= False)

def download(request, *args, **kwargs):
    params = request.GET.get('Select(number)', '')
    data = {}
    data = json.loads(params)
    recv = Wat()
    recv.province = data
    recv.select_province(recv.province)
    recv.saveCSV()
    fileName = recv.provinceName
    filePath = fileName + ".csv"
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filePath)
            return response
    else:
        return JsonResponse({"error":"404"})

@api_view(['GET'])
def downloadapi(request, *args, **kwargs):
    download_url = reverse('download')
    return Response({'download_url': download_url})