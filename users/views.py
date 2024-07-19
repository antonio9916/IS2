from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from allauth.account.auth_backends import AuthenticationBackend
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Workspace, Board, List
from .forms import TaskForm, WorkspaceForm, BoardForm, ListForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class WorkspaceListView(ListView):
    model = Workspace
    template_name = 'users/workspace_list.html'
    context_object_name = 'workspaces'

class WorkspaceDetailView(DetailView):
    model = Workspace
    template_name = 'users/workspace_detail.html'

class WorkspaceCreateView(CreateView):
    model = Workspace
    form_class = WorkspaceForm
    template_name = 'users/workspace_form.html'
    success_url = reverse_lazy('workspace_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class WorkspaceUpdateView(UpdateView):
    model = Workspace
    form_class = WorkspaceForm
    template_name = 'users/workspace_form.html'
    success_url = reverse_lazy('workspace_list')

class WorkspaceDeleteView(DeleteView):
    model = Workspace
    template_name = 'users/workspace_confirm_delete.html'
    success_url = reverse_lazy('workspace_list')
    
@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

@method_decorator(login_required, name='dispatch')
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'user']  # Asegúrate de incluir el campo 'user'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed', 'user']  # Asegúrate de incluir el campo 'user'
    success_url = reverse_lazy('task_list')

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

class TaskListView(ListView):
    model = Task
    template_name = 'users/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'users/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'users/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'users/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'users/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
def home(request):
    return render(request, 'users/home.html')  # Asegúrate de tener esta plantilla
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class BoardListView(ListView):
    model = Board
    template_name = 'users/board_list.html'

class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'users/board_form.html'
    success_url = reverse_lazy('board_list')

class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'users/board_form.html'
    success_url = reverse_lazy('board_list')

class BoardDeleteView(DeleteView):
    model = Board
    template_name = 'users/board_confirm_delete.html'
    success_url = reverse_lazy('board_list')

class ListCreateView(CreateView):
    model = List
    form_class = ListForm
    template_name = 'users/list_form.html'
    success_url = reverse_lazy('board_list')

class ListUpdateView(UpdateView):
    model = List
    form_class = ListForm
    template_name = 'users/list_form.html'
    success_url = reverse_lazy('board_list')

class ListDeleteView(DeleteView):
    model = List
    template_name = 'users/list_confirm_delete.html'
    success_url = reverse_lazy('board_list')