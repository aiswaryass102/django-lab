from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/<str:message>/', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
]