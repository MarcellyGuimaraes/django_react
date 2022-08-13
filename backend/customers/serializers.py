from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_of_birth',)
        read_only_fields = ('id',)
