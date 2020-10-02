from . import models

from rest_framework import serializers


class SubjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubjectModel
        fields = (
            'pk', 
            'name', 
            'code', 
            'branch', 
            'units', 
        )


