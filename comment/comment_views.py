from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CommentForm
from .models import Comment


class CommentView(TemplateView):
    http_method_names = ["post"]
    template_name = "comment/result.html"

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get("target")

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)  # 设置了commit之后数据不会直接保存 而是会返回一个对象，可以在这个对象上再增加修改数据，然后再保存
            instance.target = target
            instance.status = Comment.STATUS_DELETE  # 默认为不可见 管理员设置后为可见
            instance.save()
            succeed = True
            # return redirect(target)
        else:
            succeed = False
        context = {
            "succeed": succeed,
            "form": comment_form,
            "target": target
        }
        return self.render_to_response(context)
