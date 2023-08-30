from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model =  Post
    template_name = 'blog/home.html'
    ordering = ['-data_publicacao']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoriaListView(request):
    cat_menu_list = Categoria.objects.all()
    return render(request, 'blog/categories_list.html', {'cat_menu_list':cat_menu_list})

def CategoriaView(request, cats):
    categoria_posts = Post.objects.filter(categoria=cats.title().replace('-',' '))
    print(categoria_posts)
    return render(request, 'blog/categories.html', {'categoria':cats.title().replace('-',' '), 'category_post': categoria_posts})

class PostView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'

class NewCategoria(CreateView):
    model = Categoria
    template_name = 'blog/new_categorys.html'
    fields = ['nome']


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')