from django.shortcuts import render

def form_view(request):
    return render(request, 'form.html')


def result_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        color = request.POST.get('color')
        data = request.POST

        return render(request, 'result.html', {
            'name': name,
            'color': color,
            'data': data
        })
    else:
        return render(request, 'form.html')