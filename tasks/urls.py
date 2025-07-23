from django.urls import path
from tasks.views import admindashboard,text,create_task,view_task
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns=[
    path('admindashboard/',admindashboard),
    path('text/',text),
    path('create-task/',create_task),
    path('view_task/',view_task)
]+ debug_toolbar_urls()