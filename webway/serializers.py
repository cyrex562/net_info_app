from rest_framework import serializers

from .models import *


# class ProtocolSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Protocol
#         fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class NetworkAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkAddress
        fields = "__all__"


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = "__all__"


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = "__all__"



