from rest_framework import serializers
from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('visitor', 'login_date', 'logout_date')