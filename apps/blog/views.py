from django.shortcuts import render
from apps.blog.models import Category, Post
# Create your views here.
from django.views.generic import ListView


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context
