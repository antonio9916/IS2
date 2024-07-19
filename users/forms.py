from django import forms
from .models import Task, Workspace, Board, List

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'assigned_to']
class WorkspaceForm(forms.ModelForm):
    class Meta:
        model = Workspace
        fields = ['name', 'description']
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'workspace']

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'board', 'max_wip']