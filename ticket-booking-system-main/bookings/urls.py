from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    BookingCreateView,
    MyBookingsView,
    AdminAddEventView,
    RegisterView,
    ProfileView,
)
from django.contrib.auth.views import LogoutView  # Add this import

urlpatterns = [
    # Public routes
    path('', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    
    # Authenticated user routes
    path('book/<int:pk>/', BookingCreateView.as_view(), name='book_event'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    
    # Auth routes
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Add this line
    
    # Admin routes
    path('admin/add-event/', AdminAddEventView.as_view(), name='add_event'),
]