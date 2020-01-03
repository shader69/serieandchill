from django import forms
from app.models import Comment


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'serie',
            'creator',
            'rate',
            'content',
            'postdate'
        ]
