from django.http import HttpResponse
from octo_nemesis.views.json_response import JSONResponse 
from rest_framework.parsers import JSONParser

from octo_nemesis.models import StateSet
from octo_nemesis.serializers import StateSetSerializer

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status

@csrf_exempt
def stateset_list(request):
    """
    List all StateSets by name, or create a new StateSet.
    """
    if request.method == 'GET':
        statesets = StateSet.objects.all()
        serializer = StateSetSerializer(statesets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StateSetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def stateset_detail(request, pk):
    """
    Retrieve, update or delete a StateSet.
    """
    try:
        stateset = StateSet.objects.get(pk=pk)
    except StateSet.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StateSetSerializer(stateset)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StateSetSerializer(stateset, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stateset.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)        
        
        