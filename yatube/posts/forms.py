from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text', 'author')
        labels = {
            'group': 'Группа.',
            'text': 'Текст поста.',
        }
