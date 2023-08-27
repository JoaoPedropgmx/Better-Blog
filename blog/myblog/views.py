from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model =  Post
    template_name = 'blog/home.html'
    ordering = ['-data_publicacao']

class PostView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post.html'

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/edit.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')