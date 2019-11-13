from django.shortcuts import render
from .models import Post,Hot

def index(request):
    post_list=Post.objects.all()
    return render(request, 'blog/index.html', context={
        'post_list':post_list
    })
