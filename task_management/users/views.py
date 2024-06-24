from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')  # Asegúrate de tener esta plantilla
