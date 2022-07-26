from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
        """Serializes a anem field for testing our APIView"""
        name = serializers.CharField(max_length=10)
