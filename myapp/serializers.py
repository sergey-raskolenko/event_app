from rest_framework import serializers
from myapp.models import User, Event, Organization


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class OrganizationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('title', 'address', 'postcode', 'users')


class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
