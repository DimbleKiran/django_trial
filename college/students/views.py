from rest_framework.views import APIView                            # to view good look
from rest_framework.response import Response                        # tp create response in json
from branch.models import Mechanical
from rest_framework import status
from .serializers import MechanicalSer


class StudentRest(APIView):
    def get(self, r):
        obj = Mechanical.objects.all()              # in obj data will receive in queryset
        serobj = MechanicalSer(obj, many=True)      # pass queryset to serializer module created, it gives json object
        return Response(serobj.data)

    def post(self, r):
        # in post client sends the data, that data we need to catch in post
        # data come through post is in json format
        # we need to serialize the data to queryset & dump to database
        obj = MechanicalSer(data=r.data)                 # we pass request+data came from POST to deserializer
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=status.HTTP_201_CREATED)
        return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentUpdDel(APIView):
    def put(self, r, pk):
        obj = Mechanical.objects.get(pk=pk)
        serobj = MechanicalSer(obj, data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data, status=status.HTTP_201_CREATED)
        return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, r, pk):
        obj = Mechanical.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
