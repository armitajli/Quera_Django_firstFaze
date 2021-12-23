from django.shortcuts import render

from accounts.models import User


def about_us(request):
    if request.method == "GET":
        members = User.objects.all()
        return render(request, 'about_us.html', {'members': members})
