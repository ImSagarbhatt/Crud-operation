from .models import TodoModel
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = "__all__"
