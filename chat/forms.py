from django import forms
from chat.models import Question


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
