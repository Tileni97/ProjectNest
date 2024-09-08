from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('projects/', include('project.urls')),
    path('projects/<uuid:project_id>/', include('Todolist.urls')),
    path('projects/<uuid:project_id>/<uuid:Todolist_id>/', include('task.urls')),

]