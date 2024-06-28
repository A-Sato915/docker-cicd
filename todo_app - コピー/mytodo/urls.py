from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index, name="index"),
    path("add/", mytodo.add,name="add"),
    path("Update_task_complete/", mytodo.Update_task_complete, name="Update_task_complete")
]