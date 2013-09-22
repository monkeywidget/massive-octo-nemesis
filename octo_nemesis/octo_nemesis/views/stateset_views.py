from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from octo_nemesis.models.stateset_model import StateSet
from octo_nemesis.serializers import StateSetSerializer


@api_view(['GET', 'POST'])
def stateset_list(request):
    """
    List all StateSets, or create a new StateSet.
    """
    if request.method == 'GET':
        statesets = StateSet.objects.all()
        serializer = StateSetSerializer(statesets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StateSetSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stateset_detail(request, pk):
    """
    Retrieve, update or delete a StateSet.
    """
    try:
        stateset = StateSet.objects.get(pk=pk)
    except StateSet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StateSetSerializer(stateset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StateSetSerializer(stateset, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        stateset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
        
        