from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "Aiswarya", "grade": "A", "passed": True},
        {"name": "Rahul", "grade": "C", "passed": True},
        {"name": "Meera", "grade": "F", "passed": False},
    ]

    return render(request, "student_list.html", {"students": students})