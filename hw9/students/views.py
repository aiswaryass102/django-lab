from django.shortcuts import render, redirect

students_data = ["Aiswarya", "Rahul", "Anu"]

def student_list(request, message):
    return render(request, 'students/list.html', {
        'students': students_data,
        'message': message
    })

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        students_data.append(name)

        return redirect('students:list', message="Student Added Successfully!")

    return render(request, 'students/add.html')