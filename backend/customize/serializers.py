from rest_framework import serializers

from .models import Customize


class CustomizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customize
        fields = "__all__"
