from django.shortcuts import render, redirect

teachers_data = ["Mr. Kumar", "Ms. Devi"]

def teacher_list(request, message):
    return render(request, 'teachers/list.html', {
        'teachers': teachers_data,
        'message': message
    })

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teachers_data.append(name)

        return redirect('teachers:list', message="Teacher Added Successfully!")

    return render(request, 'teachers/add.html')