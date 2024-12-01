from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import YogaClass
from .forms import ContactForm, BookingForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

# Home Page
def home(request):
    return render(request, 'app/index.html')

# Courses Page
def base(request):
    classes = YogaClass.objects.all()
    return render(request, 'app/base.html', {'classes': classes})

# About Page
def about(request):
    return render(request, 'app/about.html')

# Contact Page
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email logic
            send_mail(
                f'{subject} from {name}',  # Subject
                message,  # Message
                email,  # From email
                ['your_email@example.com'],  # To email (replace with yours)
                fail_silently=False
            )
            return render(request, 'app/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})

# Booking View
def book_class(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = BookingForm(data)
            if form.is_valid():
                booking = form.save()  # Save to SQLite

                # Prepare email content
                subject_user = 'Your Yoga Class Booking Confirmation'
                message_user = f"""Hi {booking.user_name},

Thank you for booking the {booking.service.capitalize()} class scheduled on {booking.date} at {booking.time}.

Location: {booking.location.capitalize()}
Instructor: {booking.instructor.capitalize()}

See you there!

Best regards,
YogaFlex Team"""

                subject_admin = 'New Yoga Class Booking'
                message_admin = f"""New booking details:

User Name: {booking.user_name}
Email: {booking.user_email}
Phone: {booking.phone}
Service: {booking.service.capitalize()}
Location: {booking.location.capitalize()}
Instructor: {booking.instructor.capitalize()}
Date: {booking.date}
Time: {booking.time}"""

                # Send email to user
                send_mail(
                    subject_user,
                    message_user,
                    settings.DEFAULT_FROM_EMAIL,
                    [booking.user_email],
                    fail_silently=False,
                )

                # Send email to admin
                send_mail(
                    subject_admin,
                    message_admin,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )

                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid data'}, status=400)
        except Exception as e:
            # Optionally log the error
            print(f"Error processing booking: {e}")
            return JsonResponse({'success': False, 'error': 'An unexpected error occurred.'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
