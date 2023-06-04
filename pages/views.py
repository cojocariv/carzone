from django.shortcuts import redirect, render
from cars.models import Car
from django.core.mail import send_mail
from pages.models import Team
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    condition_search = Car.objects.values_list('condition', flat=True).distinct()

    data = {
        "teams": teams,
        "featured_cars": featured_cars,
        "all_cars": all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'condition_search': condition_search,
    }
    return render(request, "pages/home.html", data)


def about(request):
    teams = Team.objects.all()
    data = {
        "teams": teams,
    }
    return render(request, "pages/about.html", data)


def services(request):
    return render(request, "pages/services.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
    
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone' + phone + '. Message: ' + message

        send_mail(
            subject,
            message_body,
            'cojocari.v@mail.ru',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, "pages/contact.html")
