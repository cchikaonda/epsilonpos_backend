# apps/accounts/serializers.py
from rest_framework import serializers
from apps.accounts.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'email', 'full_name', 'user_role', 'phone_number',
            'active', 'admin', 'superuser', 'staff', 'timestamp', 'image',
            'group', 'description', 'imageURL'
        )
        read_only_fields = ('id', 'timestamp', 'imageURL')
