from django.http import JsonResponse, HttpResponse
import json
from getData import Wat 
import os

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.load(body)
    except:
        pass

    return JsonResponse({"what": "its working huh"})

def select(request, *args, **kwargs):
    body = request.body
    data = {}
    data = json.loads(body)
    recv = Wat()
    recv.province = data["Select(number)"]
    recv.select_province(recv.province)
    return JsonResponse({"list": recv.data})

def download(request, *args, **kwargs):
    body = request.body
    data = {}
    data = json.loads(body)
    recv = Wat()
    recv.province = data["Select(number)"]
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
