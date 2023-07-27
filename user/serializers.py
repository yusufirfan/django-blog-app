from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())], style={'input_type': 'email'})
    password = serializers.CharField(required=True,write_only=True,validators=[validate_password], style={'input_type': 'password'})
    password2 = serializers.CharField(required=True,write_only=True,validators=[validate_password], style={'input_type': 'password'})

    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'password2'

    def validate(self, attrs):
        if attrs['password'] == attrs['password2']:
            return super().validate(attrs)
        raise serializers.ValidationError({'password' : 'Please check your passwords.'})

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get('username'),
            email = validated_data.get('email'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return super().create(validated_data)
