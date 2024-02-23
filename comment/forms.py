from django import forms
import mistune

from .models import Comment


class CommentForm(forms.ModelForm):
    """评论表单"""
    nickname = forms.CharField(
        label="昵称",
        max_length=50,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "style": "width: 60%;"}
        )
    )
    email = forms.CharField(
        label="Email",
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control", "style": "width: 60%;"}
        )
    )
    website = forms.CharField(
        label="网站",
        max_length=100,
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control", "style": "width: 60%;"}
        )
    )
    content = forms.CharField(
        label="内容",
        max_length=500,
        widget=forms.widgets.Textarea(
            attrs={"rows": 6, "cols": 60, "class": "form-control"}
        )
    )

    def clean_content(self):
        """使用钩子方法对评论字数进行验证"""
        content = self.cleaned_data.get("content")
        if len(content) < 10:
            raise forms.ValidationError("太短啦，多说一点吧")
        content = mistune.markdown(content)
        return content

    class Meta:
        model = Comment
        fields = ["nickname", "email", "website", "content"]
