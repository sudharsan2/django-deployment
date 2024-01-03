from rest_framework import serializers
from l1_support.models import error_code

class error_code_serializer(serializers.ModelSerializer):
    class Meta:
        model = error_code
        fields = "__all__"
