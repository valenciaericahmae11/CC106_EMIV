from django.shortcuts import render  # type: ignore[import-not-found]


def landing(request):
    return render(request, 'home/landing.html')


def home(request):
    context = {
        'title': 'My Home Page',
        'message': 'Welcome to my first Django application!',
        'show_message': True,
    }

    return render(request, 'home/home.html', context)