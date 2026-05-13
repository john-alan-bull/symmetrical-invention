from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Activity
from .serializers import ActivitySerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'activities': reverse('activity-list', request=request, format=format)
    })


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-created_at')
    serializer_class = ActivitySerializer
