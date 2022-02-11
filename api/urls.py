from django.urls import path

from . import views


urlpatterns = [
    path('students/',views.get_details),
    path('students/<int:pk>/',views.get_detail),
    path('student-create/',views.create_detail),
    path('student-update/<int:pk>/',views.update_detail),
    path('student-delete/<int:pk>/',views.delete_detail),
]