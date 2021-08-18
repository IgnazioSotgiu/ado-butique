from django.shortcuts import render


def profile(request):
    # displays the user's profile
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
