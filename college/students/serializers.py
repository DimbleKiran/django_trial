from rest_framework import serializers
from branch.models import Mechanical


class MechanicalSer(serializers.ModelSerializer):
    class Meta:
        model = Mechanical
        fields = '__all__'
