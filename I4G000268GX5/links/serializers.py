from dataclasses import field
from links.models import Link
from rest_framework import serializers

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
