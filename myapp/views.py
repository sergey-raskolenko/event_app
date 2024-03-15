from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Event
from .serializers import OrganizationSerializer, EventSerializer, EventFilterSerializer
from myapp.tasks import create_event_with_delay


class OrganizationCreateView(generics.CreateAPIView):
    """Контроллер для создания организации"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]


class EventCreateView(generics.CreateAPIView):
    """Контроллер для создания мероприятия"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event_data = serializer.validated_data

        create_event_with_delay.delay(event_data)


class EventWithUsersListView(generics.ListAPIView):
    """
    Контроллер для получения списка всех мероприятий с информацией о всех действующих пользователей,
    которые участвуют в организации мероприятия.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class EventFilteredListView(generics.ListAPIView):
    """
    Контроллер для вывода списка всех мероприятий.
    Доступна сортировка, фильтрация по дате, поиск по названию, лимитная пагинация.
    """
    queryset = Event.objects.all()
    serializer_class = EventFilterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['date']
    ordering_fields = ['date']
    pagination_class = LimitOffsetPagination
