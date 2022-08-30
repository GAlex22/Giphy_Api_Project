from rest_framework import serializers
from base.models import Search

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'
        read_only_fields = ('url')