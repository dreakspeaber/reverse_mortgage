from rest_framework import serializers

class ReverseMortgageSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    property_value = serializers.IntegerField()
