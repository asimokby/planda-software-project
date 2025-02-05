from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "planner"

urlpatterns = [
    # /planner/dashboard
    # path("dashboard/", views.ProjectView.as_view(), name="project_page"),
    # TODO: remove "planner" from all urls

    # /planner/projects/
    path("projects/", views.ProjectCreateView.as_view(), name="projects_listed"),  # lists user's projects

    # /planner/project/<project_id>
    path("project/<int:project_id>", views.ProjectWithCategoryCreate.as_view(), name="project_page"),
    # DELETE PROJECT
    path("delete/project/<int:project_id>", views.ProjectDeleteView.as_view(), name="delete_project"),
    # /planner/dashboard/
    # path("dashboard/", views.DashboardView.as_view(), name="dashboard"), # commented for testing
    # ADD TASK: /planner/project/<project_id>/category/<category_id>/add/task/
    path("project/<int:project_id>/category/<int:category_id>/add/task/", views.TaskCreate.as_view(), name="add_task"),
    # /planner/<task_id>/delete/
    path("project/<int:project_id>/delete/task/<int:task_id>/", views.TaskDelete.as_view(), name="delete_task"),
    # UPDATE TASK: /planner/project/<project_id>/update/task/<task_id>/
    path("project/<int:project_id>/update/task/<int:task_id>/", views.TaskUpdate.as_view(), name="update_task"),
    # TASK DETAILS: /planner/project/<project_id>/task/<task_id>/
    path("project/<int:project_id>/task/<int:pk>/", views.DetailView.as_view(), name="detail"),

    # ADD USER
    path("project/<int:project_id>/add/user/<str:new_username>/", views.ProjectUpdateView.as_view(), name="add_user")



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
