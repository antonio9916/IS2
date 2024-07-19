from django.urls import path, include
from django.contrib import admin
from . import views
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, WorkspaceListView, WorkspaceDetailView, WorkspaceCreateView, WorkspaceUpdateView, WorkspaceDeleteView, BoardListView, BoardCreateView, BoardUpdateView, BoardDeleteView, ListCreateView, ListUpdateView, ListDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Para el manejo de autenticación con allauth
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Ruta para la página de inicio
    path('', views.home, name='home'),

    # Rutas para las operaciones CRUD de tareas
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('workspaces/', WorkspaceListView.as_view(), name='workspace_list'),
    path('workspaces/<int:pk>/', WorkspaceDetailView.as_view(), name='workspace_detail'),
    path('workspaces/new/', WorkspaceCreateView.as_view(), name='workspace_create'),
    path('workspaces/<int:pk>/edit/', WorkspaceUpdateView.as_view(), name='workspace_edit'),
    path('workspaces/<int:pk>/delete/', WorkspaceDeleteView.as_view(), name='workspace_delete'),
    path('boards/', BoardListView.as_view(), name='board_list'),
    path('boards/create/', BoardCreateView.as_view(), name='board_create'),
    path('boards/<int:pk>/edit/', BoardUpdateView.as_view(), name='board_update'),
    path('boards/<int:pk>/delete/', BoardDeleteView.as_view(), name='board_delete'),
    path('lists/create/', ListCreateView.as_view(), name='list_create'),
    path('lists/<int:pk>/edit/', ListUpdateView.as_view(), name='list_update'),
    path('lists/<int:pk>/delete/', ListDeleteView.as_view(), name='list_delete'),
]