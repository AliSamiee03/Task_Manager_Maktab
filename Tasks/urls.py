from django.urls import path
from .views import all_tasks_view, show_detail_view

urlpatterns = [
    path('all-tasks/', all_tasks_view, name='all'),
    path('detail-tasks/<int:task_id>', show_detail_view, name='detail'),
]
