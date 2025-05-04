from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Event, Booking

class EventListView(View):
    def get(self, request):
        events = Event.objects.all().order_by('date')
        return render(request, 'bookings/event_list.html', {'events': events})

class EventDetailView(View):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        return render(request, 'bookings/event_detail.html', {'event': event})

class BookingCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        seats = int(request.POST.get('seats', 0))
        if seats > event.available_seats:
            return redirect('event_detail', pk=pk)
        Booking.objects.create(
            user=request.user,
            event=event,
            num_seats=seats
        )
        event.available_seats -= seats
        event.save()
        return redirect('my_bookings')

class MyBookingsView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

class AdminAddEventView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('event_list')
        return render(request, 'bookings/admin_add_event.html')
    
    def post(self, request):
        Event.objects.create(
            title=request.POST.get('title'),
            date=request.POST.get('date'),
            venue=request.POST.get('venue'),
            total_seats=int(request.POST.get('total_seats')),
            available_seats=int(request.POST.get('total_seats')),
            image_url=request.POST.get('image_url', '')
        )
        return redirect('event_list')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'bookings/profile.html', {
            'user': request.user,
            'bookings': Booking.objects.filter(user=request.user).select_related('event')
        })