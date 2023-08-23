from django.urls import path
from .views import blog_list, blog_detail, blog_delete

urlpatterns = [
    path('',blog_list),
    path('<int:id>/', blog_detail),
    path('<int:id>/delete/', blog_delete),
]