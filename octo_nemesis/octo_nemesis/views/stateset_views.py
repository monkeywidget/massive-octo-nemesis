from octo_nemesis.models.stateset_model import StateSet
from octo_nemesis.serializers import StateSetSerializer

from octo_nemesis.views.mixins.jsonresponse import JSONResponseMixin

from rest_framework import mixins
from rest_framework import generics

# http://django-rest-framework.org/tutorial/3-class-based-views.html
class StateSetList(JSONResponseMixin, generics.ListCreateAPIView):
    queryset = StateSet.objects.all()
    serializer_class = StateSetSerializer


# We need the more verbose mixin version here
# because we need to render details for the "get" method 
# ... otherwise we could have used generics.RetrieveUpdateDestroyAPIView
# 
# http://django-rest-framework.org/tutorial/3-class-based-views.html
class StateSetDetail(JSONResponseMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):

    queryset = StateSet.objects.all()
    serializer_class = StateSetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''  The other format:
http://django-rest-framework.org/tutorial/2-requests-and-responses.html

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

...

using urls.py

    
    # url(r'^statesets/$', 'stateset_list'),
    # url(r'^statesets/(?P<pk>[0-9]+)/?$', 'stateset_detail')

'''
