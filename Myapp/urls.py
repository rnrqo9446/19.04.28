from django.contrib import admin
from django.urls import path
import Myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', Myapp.views.home, name = 'home'),
    path('new', Myapp.views.new, name = 'new'),
    path('<int:post_id>/detail', Myapp.views.detail, name = 'detail'),
    path('<int:post_id>/edit', Myapp.views.edit, name = 'edit'),
    path('<int:post_id>/delete', Myapp.views.delete, name = 'delete'),
]
