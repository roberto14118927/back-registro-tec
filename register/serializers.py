from rest_framework import serializers

from register.models import Register
from register.models import Teams

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('__all__')

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('__all__')
        