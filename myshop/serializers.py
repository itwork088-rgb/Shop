from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    in_stock = serializers.BooleanField()