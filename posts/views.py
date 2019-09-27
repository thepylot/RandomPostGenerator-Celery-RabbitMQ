from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post
from .forms import RandomPostGeneratorForm
from .tasks import create_random_posts

def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def generate_view(request):
    form = RandomPostGeneratorForm(request.POST)
    if form.is_valid():
        number_of_posts = form.cleaned_data.get('number_of_posts')
        #executing this function in the background
        create_random_posts.delay(number_of_posts)
        messages.success(request, 'Random posts generated! Refresh the page after few seconds to see result.')
        return redirect('posts')
    return render(request, 'generate.html', {'form':form})



        