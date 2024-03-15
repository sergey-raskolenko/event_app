from rest_framework import serializers
from myapp.models import User, Event, Organization


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя с выводом его почты.
    """

    class Meta:
        model = User
        fields = ('email',)


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Сериализатор организации с выводом всех ее сотрудников.
    """
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('title', 'address', 'postcode', 'users')


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор мероприятия с вложенным выводом организаций и пользователей
    """
    organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class EventFilterSerializer(serializers.ModelSerializer):
    """
    Сериализатор мероприятия для простого вывода
    """

    class Meta:
        model = Event
        fields = '__all__'
