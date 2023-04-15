from django.http import JsonResponse
import json
import getData

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.load(body)
    except:
        pass

    return JsonResponse({"what": "its working huh"})
