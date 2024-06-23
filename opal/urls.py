from django.urls import path,include
from homepage import views,admin
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
]

#     path('login/', views.login_view, name='login'),
#     path('register/', views.register, name='register'),
#     path('logout/', views.logout_view, name='logout'),
#     path('todo/', views.todo_list, name='todo_list'),
#     path('add-task/', views.add_task, name='add_task'),
#     path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
#     path('complete-task/<int:pk>/', views.complete_task, name='complete_task'),
#     path('task/<int:pk>/', views.task_detail, name='task_detail'),
