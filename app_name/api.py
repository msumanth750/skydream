from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SubjectModelViewSet(viewsets.ModelViewSet):
    """ViewSet for the SubjectModel class"""

    queryset = models.SubjectModel.objects.all()
    serializer_class = serializers.SubjectModelSerializer
    permission_classes = [permissions.IsAuthenticated]


