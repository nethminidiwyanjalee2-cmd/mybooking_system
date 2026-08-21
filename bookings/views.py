from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service, Booking

# Service List View
def service_list(request):
    services = Service.objects.all()
    return render(request, 'bookings/service_list.html', {'services': services})

# Book Service View (Business Logic: Double Booking Check)
@login_required
def book_service(request, service_id):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=service_id)
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')

        # Double booking පරීක්ෂා කිරීම (Business Logic)
        existing_booking = Booking.objects.filter(
            service=service,
            booking_date=booking_date,
            booking_time=booking_time
        ).exists()

        if existing_booking:
            messages.error(request, 'Sorry, this time slot is already booked for this service!')
        else:
            Booking.objects.create(
                user=request.user,
                service=service,
                booking_date=booking_date,
                booking_time=booking_time,
                status='Pending'
            )
            messages.success(request, 'Booking request submitted successfully!')
            return redirect('my_bookings')

    return redirect('service_list')

# Customer's My Bookings View
@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': user_bookings})