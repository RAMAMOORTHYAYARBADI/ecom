from rest_framework import serializers
from .models import *

class ProductMstrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMstr
        fields = '__all__'