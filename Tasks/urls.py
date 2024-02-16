from django.urls import path
from .views import all_tasks_view, show_detail_view, task_complete_view, show_categories_view

urlpatterns = [
    path('all-tasks/', all_tasks_view, name='all'),
    path('detail-tasks/<int:task_id>/', show_detail_view, name='detail'),
    path('complete-task/<int:task_id>', task_complete_view, name='complete'),
    path('categories/', show_categories_view, name='categories'),
    # path('category-tasks/', )
]
