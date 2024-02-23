from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView

from blog.blog_views import CommonViewMixin
from .models import Link


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.get_links()
    template_name = "config/links.html"
    context_object_name = "link_list"



