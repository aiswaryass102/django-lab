from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def form_view(request):
    return render(request, 'form.html')


def result_view(request):
    username = request.GET.get('username')
    data = request.GET

    return render(request, 'result.html', {
        'username': username,
        'data': data
    })