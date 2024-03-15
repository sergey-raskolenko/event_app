from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.apps import MyappConfig
from myapp.views import OrganizationCreateView, EventCreateView, EventWithUsersListView, EventFilteredListView

app_name = MyappConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_organization/', OrganizationCreateView.as_view(), name='create_organization'),
    path('create_event/', EventCreateView.as_view(), name='create_event'),
    path('events_with_users/', EventWithUsersListView.as_view(), name='events_with_users'),
    path('filtered_events/', EventFilteredListView.as_view(), name='filtered_events'),
]
