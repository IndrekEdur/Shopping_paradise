from django.shortcuts import render

#def session_manipulating_page(request):


def home(request):
    request.session['name'] = 'Indrek'
    username = request.session['name']

    return render(request, 'home.html', context={'username': username})