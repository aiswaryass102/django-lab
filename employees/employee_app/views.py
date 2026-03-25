from django.shortcuts import render

def employee_list(request):
    # list of employees (sample data)
    employees = [
        {"name": "Aiswarya", "job": "Developer", "salary": 50000, "full_time": True},
        {"name": "Rahul", "job": "Designer", "salary": 40000, "full_time": False},
        {"name": "Meera", "job": "Manager", "salary": 60000, "full_time": True},
    ]

    return render(request, "employees_list.html", {"employees": employees})