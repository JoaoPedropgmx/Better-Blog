from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model =  Post
    template_name = 'blog/home.html'
    ordering = ['-data_publicacao']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))

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

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes
        context = super(PostView, self).get_context_data(*args,**kwargs)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    

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