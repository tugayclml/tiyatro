from rest_framework import viewsets
from rest_framework.response import Response

from .models import Tiyatro
from .serializer import TiyatroSerializer


class TiyatroAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Tiyatro.objects.all()
        serializer = TiyatroSerializer(queryset, many=True)
        return Response(serializer.data)
